import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = ChromeOptions()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
PATH='./chromedriver.exe'
#options.headless=True

website = 'https://fantasy.iplt20.com/season/home?source=organic'
ser = Service(PATH)
wd = webdriver.Chrome(options = options, service=ser)

wd.get(website)
wd.maximize_window()



#wd.find_element(By.XPATH, '//*[@id="home-widget"]/div/div/div/div/div[2]/div[5]/div/a').click()
#WebDriverWait(wd, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="bannerDiv"]/section/div/div[2]/div[1]/div[1]/div[2]/span')))
team1 = wd.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/span').text
team2 = wd.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/div/div[3]/div[2]/span').text

df1 = pd.read_csv('../2023/linkplayers.csv')
df2 = pd.read_csv('../2023/player_points_info.csv')

dft1 = pd.read_csv(f'../2023/{team1}.csv')
dft2 = pd.read_csv(f'../2023/{team2}.csv')
com_data = pd.merge(df1, df2, on=['player_name'])
fin_data = pd.merge(com_data, dft1, on=['player_id'])
fin_data = pd.merge(fin_data, dft2, on = ['player_id'])
combined_data = pd.concat([dft1, dft2], ignore_index=True)
fin_data = pd.merge(com_data, combined_data, on=['player_id'])
fin_data = fin_data.sort_values('player_points', ascending=False)
batter_final = fin_data.loc[(fin_data['player_role'] == "Batter") | (fin_data['player_role'] == "WK Keeper - Batter")].head(4)
allrounder_final = fin_data.loc[(fin_data['player_role'] == "All-Rounder")].head(3)
bowler_final = fin_data.loc[(fin_data['player_role'] == "Bowler")].head(4)
final_squad = pd.concat([batter_final,allrounder_final,bowler_final], ignore_index=True)

print(final_squad['player_name_x'])