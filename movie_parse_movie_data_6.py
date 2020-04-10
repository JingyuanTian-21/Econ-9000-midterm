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
	# print(mojo_table)
	
	movie_name = soup.find("h1", {"class":"a-size-extra-large"}).text
	# print(movie_name)


	opening_money = mojo_table.find("span", text=re.compile("Opening"))
	if opening_money is None:
		opening_money = "na"
	else:
		opening_money = mojo_table.find("span", text=re.compile("Opening")).find_next("span", {"class":"money"}).text.replace(",","").replace("$","")

	# print(opening_money)

	release_date_complete = re.compile(r'bo_rl_rl">(\w\w\w \d+, \d\d\d\d)').findall(html)
	if len(release_date_complete)==2:
		start_release_date = release_date_complete[0]
		end_release_date = release_date_complete[1]
		release_date = start_release_date + "-" + end_release_date
	elif len(release_date_complete)==1:
		release_date = release_date_complete[0]
	# print(release_date)

	running_time_origin = mojo_table.find("span", text=re.compile("Running Time"))
	running_time=0
	# print(running_time_origin)
	
	if running_time_origin is None:
		running_time = "na"
		running_time_section = "na"
	else:
		running_time_section = mojo_table.find("span", text=re.compile("Running Time")).find_next("span").text
	# print(running_time_section)

		running_time_section_temp = re.findall(r"[a-z]",running_time_section)
	
		if len(running_time_section_temp) == 5:
			running_time_hr = int(re.findall(r"(\d+) hr", running_time_section)[0])
			running_time_min = int(re.findall(r"(\d+) min", running_time_section)[0])/60
			running_time = running_time_hr + running_time_min
		elif len(running_time_section_temp) == 2:
			running_time_hr = int(re.findall(r"(\d+) hr", running_time_section)[0])
			running_time = running_time_hr
		elif len(running_time_section_temp) == 3:
			running_time_min = int(re.findall(r"(\d+) min", running_time_section)[0])/60
			running_time = running_time_min

	# print(running_time)


	genres = mojo_table.find("span", text=re.compile("Genres"))
	if genres is None:
		genres = "na"
	else:
		genres = mojo_table.find("span", text=re.compile("Genres")).find_next("span").text

	mpaa = mojo_table.find("span", text=re.compile("MPAA"))
	if mpaa is None:
		mpaa = "na"
	else:
		mpaa = mojo_table.find("span", text=re.compile("MPAA")).find_next("span").text

	# print(genres)	
	# print(mpaa)	

	IMDbPro = mojo_table.find("span", text=re.compile("IMDbPro"))
	if IMDbPro is None:
		IMDbPro = "na"
	else:
		IMDbPro = mojo_table.find("span", text=re.compile("IMDbPro")).find_next("a", {"class":"a-link-normal"})["href"]
		IMDbPro_ID = re.findall(r"[a-zA-Z][a-zA-Z][0-9]+", IMDbPro)[0]


	in_release_text = mojo_table.find("span", text=re.compile("In Release")).find_next("span").text
	in_release_period = int(re.findall(r'(\d+) \w\w\w\w/', in_release_text)[0])
	# print(in_release_period)

	widest_release = mojo_table.find("span", text=re.compile("Widest Release"))
	if widest_release is None:
		widest_release = "na"
	else:
		widest_release = mojo_table.find("span", text=re.compile("Widest Release")).find_next("span").text.replace(",","").replace(" theaters","").replace(" theater","")

	df = df.append({
				'movie_name':movie_name,
				'release_date': release_date,
				'running_time':running_time,
				'opening_money':opening_money,
				'widest_release':widest_release,
				'in_release_period':in_release_period,
				'genres':genres,
				'mpaa':mpaa,
				'IMDbPro_ID':IMDbPro_ID
			}, ignore_index=True)
				

df.to_csv("mojo_parsed_files_csv/mojo_movie_data_dataset.csv")

	
	# running_time_hr = re.findall(r"(\d+) hr", running_time_text)[0]
	# print(running_time_hr)
	# if running_time_hr is None:
	# 	running_time_hr = 0
	# else:
	# 	running_time_hr = int(running_time_hr)
	
	# running_time_min = re.findall(r"(\d+) min", running_time_text)[0]
	# if running_time_min is None:
	# 	running_time_min = 0
	# else:
	# 	running_time_min = int(running_time_min)/60
	


	# if running_time_hr + running_time_min == 0:
	# 	running_time = 'na'
	# else:
	# 	running_time = running_time_hr + running_time_min
		






	# running_time_hr = int(str(re.compile(r'(\d) hr').findall(html)).replace("['","").replace("']",""))
	# running_time_min = int(re.compile(r'hr (\d+) min').findall(html)[0])/60

	# running_time = running_time_hr + running_time_min.__round__(2)
	# print(running_time_hr)
	# print(running_time_min)
	# print(running_time)

