import urllib.request
import os
import time
import pandas as pd

if not os.path.exists("mojo_deep_link_daily_html"):
	os.mkdir("mojo_deep_link_daily_html")

df = pd.read_csv("mojo_parsed_files_csv/mojo_daily_link_dataset.csv")

for link in df['mojo daily link']:
	filename = link.replace("/","").replace("?ref_=bo_di_table","")
	if os.path.exists("mojo_deep_link_daily_html/" + filename + ".html"):
		print(filename + "exists")
	else:	
		print("Downloading:" + filename)
		f = open("mojo_deep_link_daily_html/" + filename + ".html.temp","wb")
		response = urllib.request.urlopen('https://www.boxofficemojo.com'+link)
		html = response.read()
		f.write(html)
		f.close()
		os.rename("mojo_deep_link_daily_html/" + filename + ".html.temp","mojo_deep_link_daily_html/" + filename + ".html")
		time.sleep(1)


