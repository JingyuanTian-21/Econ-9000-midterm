from bs4 import BeautifulSoup
import pandas as pd
import os
import glob

if not os.path.exists("mojo_parsed_files_csv"):
	os.mkdir("mojo_parsed_files_csv")

df = pd.DataFrame()

for one_file_name in glob.glob("mojo_deep_link_daily_html/*.html"):
	print("parsing: ",one_file_name)
	f = open(one_file_name,"r",encoding = "utf-8")
	soup =  BeautifulSoup(f.read(),'html.parser')
	f.close()

	mojo_table = soup.find("table")
	mojo_rows = mojo_table.find_all("tr")

	for r in mojo_rows[1:]:
		#parse the data in daily box office html files
		mojo_date = soup.find("div", {"class":"a-section a-spacing-none"}).find("h1", {"class":"mojo-gutter"}).text.replace("Domestic Box Office For ", "")
		mojo_movie_link = r.find("a", {"class":"a-link-normal"})["href"]
		movie_name = r.find("a", {"class":"a-link-normal"}).text
		daily_gross_box_office = r.find("td", {"class":"a-text-right mojo-field-type-money mojo-estimatable"}).text.replace("$","")
		number_of_theaters = r.find("td", {"class":"a-text-right mojo-field-type-positive_integer mojo-estimatable"}).text.replace(",","")
		gross_box_office_to_date = r.find_all("td", {"class": "a-text-right mojo-field-type-money mojo-estimatable"})[2].text.replace("$","")
		number_days_release = r.find("td", {"class":"a-text-right mojo-field-type-positive_integer"}).text
		distributers = r.find("td", {"class":"mojo-field-type-release_studios"}).text
		#combine the parsed data together
		df = df.append({
				'date': mojo_date,
				'mojo movie link': mojo_movie_link,
				'movie_name': movie_name,
				'daily gross box office': daily_gross_box_office,
				'number of theaters': number_of_theaters,
				'gross box office to date': gross_box_office_to_date,
				'number of days in release': number_days_release,
				'distributers': distributers
			}, ignore_index=True)

df.to_csv("mojo_parsed_files_csv/mojo_daily_data_dataset.csv",index=False)
