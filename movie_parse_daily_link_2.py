from bs4 import BeautifulSoup
import pandas as pd
import os
import glob

if not os.path.exists("mojo_parsed_files_csv"):
	os.mkdir("mojo_parsed_files_csv")

df = pd.DataFrame()

for one_file_name in glob.glob("mojo_html_files/*.html"):
	print("parsing: ",one_file_name)
	f = open(one_file_name,"r",encoding = "utf-8")
	soup =  BeautifulSoup(f.read(),'html.parser')
	f.close()

	mojo_table = soup.find("table")
	mojo_rows = mojo_table.find_all("tr")

	for r in mojo_rows[1:]:
		#parse the link from all the 7-year box office mojo html
		mojo_daily_link = r.find("a", {"class":"a-link-normal"})["href"]

		#combine the parsed links together
		df = df.append({
				'mojo daily link': mojo_daily_link
			}, ignore_index=True)
	print(mojo_daily_link)

df.to_csv("mojo_parsed_files_csv/mojo_daily_link_dataset.csv")
