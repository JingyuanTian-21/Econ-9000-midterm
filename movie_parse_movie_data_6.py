from bs4 import BeautifulSoup
import pandas as pd
import os
import glob
import re

if not os.path.exists("mojo_parsed_files_csv"):
	os.mkdir("mojo_parsed_files_csv")

df = pd.DataFrame()

for one_file_name in glob.glob("mojo_deep_link_movie_html/*.html"):
	print("parsing: ",one_file_name)
	f = open(one_file_name, "r")
	html=f.read()
	f.close()
	soup = BeautifulSoup(html, 'html.parser')
	mojo_table = soup.find("div")

	#parse movie_name in movie html
	movie_name = soup.find("h1", {"class":"a-size-extra-large"}).text

	#parse opening_money in movie html
	opening_money = mojo_table.find("span", text=re.compile("Opening"))
	if opening_money is None:
		opening_money = "na"
	else:
		opening_money = mojo_table.find("span", text=re.compile("Opening")).find_next("span", {"class":"money"}).text.replace(",","").replace("$","")

	#parse release_date in movie html
	release_date_complete = re.compile(r'bo_rl_rl">(\w\w\w \d+, \d\d\d\d)').findall(html)
	#use length to identify different formats of release_date
	if len(release_date_complete)==2:
		start_release_date = release_date_complete[0]
		end_release_date = release_date_complete[1]
		release_date = start_release_date + " - " + end_release_date
	elif len(release_date_complete)==1:
		release_date = release_date_complete[0]

	#parse running_time in movie html
	running_time_origin = mojo_table.find("span", text=re.compile("Running Time"))
	running_time=0

	#Identify the movie website without running_time
	if running_time_origin is None:
		running_time = "na"
		running_time_section = "na"
	else:
		running_time_section = mojo_table.find("span", text=re.compile("Running Time")).find_next("span").text
		running_time_section_list = re.findall(r"[a-z]",running_time_section)
		#use length of "the letter list"('h','r','m','i','n') to identify different formats of running_time_
		if len(running_time_section_list) == 5:
			running_time_hr = int(re.findall(r"(\d+) hr", running_time_section)[0])
			running_time_min = int(re.findall(r"(\d+) min", running_time_section)[0])/60
			running_time = running_time_hr + running_time_min
		elif len(running_time_section_list) == 2:
			running_time_hr = int(re.findall(r"(\d+) hr", running_time_section)[0])
			running_time = running_time_hr
		elif len(running_time_section_list) == 3:
			running_time_min = int(re.findall(r"(\d+) min", running_time_section)[0])/60
			running_time = running_time_min

	#parse genres in movie html
	genres=[]
	genres_temp = mojo_table.find("span", text=re.compile("Genres"))
	if genres_temp is None:
		genres = "na"
	else:
		genres_temp = mojo_table.find("span", text=re.compile("Genres")).find_next("span").text
		genres = str(re.findall(r'(\w+)',genres_temp)).replace("'","").replace("[","").replace("]","")
	
	#parse MPAA in movie html
	MPAA = mojo_table.find("span", text=re.compile("MPAA"))
	if MPAA is None:
		MPAA = "na"
	else:
		MPAA = mojo_table.find("span", text=re.compile("MPAA")).find_next("span").text

	#parse IMDbPro in movie html
	IMDbPro = mojo_table.find("span", text=re.compile("IMDbPro"))
	if IMDbPro is None:
		IMDbPro = "na"
	else:
		IMDbPro = mojo_table.find("span", text=re.compile("IMDbPro")).find_next("a", {"class":"a-link-normal"})["href"]
		IMDbPro_ID = re.findall(r"[a-zA-Z][a-zA-Z][0-9]+", IMDbPro)[0]

	#parse in_release_period in movie html
	in_release_text = mojo_table.find("span", text=re.compile("In Release")).find_next("span").text
	in_release_period = int(re.findall(r'(\d+) \w\w\w\w/', in_release_text)[0])

	#parse widest_release in movie html
	widest_release = mojo_table.find("span", text=re.compile("Widest Release"))
	if widest_release is None:
		widest_release = "na"
	else:
		widest_release = mojo_table.find("span", text=re.compile("Widest Release")).find_next("span").text.replace(",","").replace(" theaters","").replace(" theater","")

	#combine the parsed data together
	df = df.append({
				'movie_name':movie_name,
				'release_date': release_date,
				'running_time':running_time,
				'opening_money':opening_money,
				'widest_release':widest_release,
				'in_release_period':in_release_period,
				'genres':genres,
				'MPAA':MPAA,
				'IMDbPro_ID':IMDbPro_ID
			}, ignore_index=True)
				
df.to_csv("mojo_parsed_files_csv/mojo_movie_data_dataset.csv",index=False)

	# running_time_hr = int(str(re.compile(r'(\d) hr').findall(html)).replace("['","").replace("']",""))
	# running_time_min = int(re.compile(r'hr (\d+) min').findall(html)[0])/60

	# running_time = running_time_hr + running_time_min.__round__(2)
	# print(running_time_hr)
	# print(running_time_min)
	# print(running_time)

