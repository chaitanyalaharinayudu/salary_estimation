import webscraper as gs 
import pandas as pd 

path = "C:/Users/Input your file path/Documents/salary_estimation/chromedriver" #path of the file

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
