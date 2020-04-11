"# Econ-9000-midterm" 
This is a readme for Jingyuan Tian's Econ-9000-midterm project.

The first python file we need to run is "movie_request_1.py". This file "movie_request_1.py" is to request the 7-year box office mojo html files and puts them in the "mojo_html_files" folder.

The second python file we need to run is "movie_parse_daily_link_2.py". In this python file, I parse the links from all the 7-year box office mojo html, and then I combine the parsed links together to form up a csv file called "mojo_daily_link_dataset.csv" under the folder "mojo_parsed_files_csv".

The third python file we need to run is "movie_deeplink_request_daily_3.py". In this file, I use the movie links in "mojo_daily_link_dataset.csv" to request daily box office html files, and put all the daily html files in the folder "mojo_deep_link_daily_html".

The fourth python file we need to run is "movie_parse_daily_data_4.py". In this file, I parse the required data in daily box office html files and combine the parsed data into a csv file called "mojo_daily_data_dataset.csv" in the folder "mojo_parsed_files_csv".

The fifth python file we need to run is "movie_deeplink_request_movie_5.py". In this file, I use the movie links in the "mojo_daily_data_dataset.csv" to request all the movie html files, and I save all the movie html files in the folder "mojo_deep_link_movie_html".

The sixth python file we need to run is "movie_parse_movie_data_6.py". In this file, I parse the required data in movie html files and combine the parsed data into a csv file called "mojo_movie_data_dataset.csv" in the folder "mojo_parsed_files_csv".

The final python file we need to run is "movie_daily_combine_7.py". In this file, we can emerge "mojo_daily_data_dataset.csv" with "mojo_movie_data_dataset.csv" by using movie names. Finally, we will have a combined dataset which is the same as the sample dataset.
