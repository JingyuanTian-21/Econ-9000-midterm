import urllib.request
import os
import time
import pandas as pd
import re

if not os.path.exists("mojo_deep_link_movie_html"):
	os.mkdir("mojo_deep_link_movie_html")

df = pd.read_csv("mojo_parsed_files_csv/mojo_daily_data_dataset.csv")

for movie_link in df['mojo movie link']:
	filename = re.findall(r"[0-9]+", movie_link)[0]
	if os.path.exists("mojo_deep_link_movie_html/" + filename + ".html"):
		print(filename + "exists")
	else:	
		#request all the movie html
		print("Downloading:" + filename)
		f = open("mojo_deep_link_movie_html/" + filename + ".html.temp","wb")
		response = urllib.request.urlopen('https://www.boxofficemojo.com'+ movie_link)
		html = response.read()
		f.write(html)
		f.close()
		os.rename("mojo_deep_link_movie_html/" + filename + ".html.temp","mojo_deep_link_movie_html/" + filename + ".html")
		time.sleep(1)

