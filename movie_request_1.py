import urllib.request
import os
import time

if not os.path.exists("mojo_html_files"):
	os.mkdir("mojo_html_files")

mojo_year=[2014,2013,1996,1997,1998,2008,2009]
url_list = []

for each_year in mojo_year:
	url = f'{"https://www.boxofficemojo.com/daily/"}{each_year}{"/?view=year"}'
	url_list.append(url)
	string_mojoyear=str(mojo_year)

for i in range(7):
	#request the 7-year box office mojo html
	f = open("mojo_html_files/box_office_mojo_movie" + string_mojoyear[(i-1)*6+1:(i-1)*6+5] + ".html", "wb")
	response = urllib.request.urlopen(url_list[i-1])
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(5)


# # request box office mojo 2014 html
# f = open("mojo_html_files/movie2014.html", "wb")
# response = urllib.request.urlopen("https://www.boxofficemojo.com/daily/2014/?view=year")
# html = response.read()
# f.write(html)
# f.close()
# time.sleep(10)

# # request box office mojo 2013 html
# f = open("mojo_html_files/movie2013.html", "wb")
# response = urllib.request.urlopen("https://www.boxofficemojo.com/daily/2013/?view=year")
# html = response.read()
# f.write(html)
# f.close()
# time.sleep(10)

# # request box office mojo 1996 html
# f = open("mojo_html_files/movie1996.html", "wb")
# response = urllib.request.urlopen("https://www.boxofficemojo.com/daily/1996/?view=year")
# html = response.read()
# f.write(html)
# f.close()
# time.sleep(10)

# # request box office mojo 1997 html
# f = open("mojo_html_files/movie1997.html", "wb")
# response = urllib.request.urlopen("https://www.boxofficemojo.com/daily/1997/?view=year")
# html = response.read()
# f.write(html)
# f.close()
# time.sleep(10)

# # request box office mojo 1998 html
# f = open("mojo_html_files/movie1998.html", "wb")
# response = urllib.request.urlopen("https://www.boxofficemojo.com/daily/1998/?view=year")
# html = response.read()
# f.write(html)
# f.close()
# time.sleep(10)

# # request box office mojo 2008 html
# f = open("mojo_html_files/movie2008.html", "wb")
# response = urllib.request.urlopen("https://www.boxofficemojo.com/daily/2008/?view=year")
# html = response.read()
# f.write(html)
# f.close()
# time.sleep(10)

# # request box office mojo 2009 html
# f = open("mojo_html_files/movie2009.html", "wb")
# response = urllib.request.urlopen("https://www.boxofficemojo.com/daily/2009/?view=year")
# html = response.read()
# f.write(html)
# f.close()
# time.sleep(10)
