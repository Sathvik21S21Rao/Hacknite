from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
def fetch_year_wise(year,team,team_acr):
    PATH="/usr/bin/chromedriver.exe"
    options=ChromeOptions()
    options.headless=True
    ser=Service(PATH)
    Wd=webdriver.Chrome(service=ser,options=options)
    Wd.maximize_window()
    Wd.get(f"https://www.iplt20.com/teams/{team}/squad/{year}#list")
    time.sleep(2)
    player_names=[i.text for i in Wd.find_elements(By.XPATH,"//div[@class='ih-p-name']")]
    player_id=[]
    for i in range(len(player_names)):
        player_id.append(f"{team_acr}{100+i}")
    player_roles=[i.text for i in Wd.find_elements(By.XPATH,"//span[@class='d-block w-100 text-center']")]
    player_info=list(zip(player_id,player_names,player_roles))
    with open(f"./{year}/{team_acr}_players.csv","w") as fp:
        writer=csv.writer(fp)
        writer.writerow(["player_id","player_name","player_role"])
        for i in range(len(player_info)):
            writer.writerow(player_info[i])
teams = ['chennai-super-kings', 'delhi-capitals', 'gujarat-titans', 'kolkata-knight-riders', 'lucknow-super-giants', 'mumbai-indians', 'punjab-kings', 'rajasthan-royals', 'royal-challengers-bangalore', 'sunrisers-hyderabad']
teamsacr = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
teamsacr_before2022=['CSK','DC','KKR','MI','PBKS','RR','RCB','SRH']
dic=dict(zip(teamsacr,teams))
for year in range(2022,2017,-1):
    if(year<2022):
        teamlist=teamsacr_before2022
    else:
        teamlist=teamsacr
    for i in range(len(teamlist)):
        fetch_year_wise(year,dic[teamlist[i]],teamlist[i])

