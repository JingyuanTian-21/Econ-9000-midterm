import pandas as pd
import os

if not os.path.exists("mojo_parsed_files_csv"):
	os.mkdir("mojo_parsed_files_csv")

df_daily = pd.read_csv("mojo_parsed_files_csv/mojo_daily_data_dataset.csv")
df_movie = pd.read_csv("mojo_parsed_files_csv/mojo_movie_data_dataset.csv")

# result= pd.concat([df_daily, df_movie], axis=1, join='inner')
result = pd.merge(df_daily,df_movie,on='movie_name',how='inner').drop('mojo movie link', axis=1)

result.to_csv("mojo_parsed_files_csv/final_merged_daily_movie_dataset.csv",index=False)