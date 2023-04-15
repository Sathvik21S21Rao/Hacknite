from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
def player_pos(year,team,team_acr):
    PATH="/usr/bin/chromedriver.exe"
    ser=Service(PATH)
    Wd=webdriver.Chrome(service=ser)
    Wd.maximize_window()
    Wd.get("https://www.iplt20.com/matches")
    menu=Wd.find_elements(By.XPATH,"//a[@class='nav-link']")
    menu[0].click()
    time.sleep(3)
    Wd.find_elements(By.XPATH,"//div[@class='cSBDisplay ng-binding']")[3].click()
    time.sleep(2)
    L=Wd.find_elements(By.XPATH,'//div[@class="cSBList active"]/div')
    L[2023-year].click()
    time.sleep(2)
    menu=Wd.find_elements(By.XPATH,"//div[@class='cSBDisplay ng-binding']")[1]
    menu.click()
    time.sleep(2)
    L=Wd.find_elements(By.XPATH,'//div[@class="cSBList active"]/div')
    pos=0
    if(year<2022):
        localteam=teamsacr_before2022
    else:
        localteam=teamsacr
    for j in range(len(localteam)):
        if localteam[j]==team_acr:                
            pos=j 
            break
    
    ActionChains(Wd).move_to_element(L[0]).perform()
    Wd.execute_script("arguments[0].scrollIntoView();",menu)
    #ActionChains(Wd).move_to_element(L[pos+1]).click()
    L[pos+1].click()
    

    time.sleep(2)
    matches=Wd.find_elements(By.XPATH,"//a[@class='vn-matchBtn ng-scope']")
    for j in range(len(matches)):
        
        Wd.execute_script(f'window.scrollTo(0,{j*200});')
        time.sleep(2)
        matches[j].click()
        time.sleep(2)
        Wd.find_element(By.XPATH,"//a[@data-id='scoreCard']").click()
        time.sleep(2)
        T=Wd.find_elements(By.XPATH,"//a[@class='ap-inner-tb-click ng-binding ng-scope']")
        for k in range(2):
            if team_acr in (T[k].text).upper() or team in (T[k].text).lower() :
                T[k].click()
                time.sleep(2)
        positions=[k.text for k in Wd.find_elements(By.XPATH,'//span[@class="ng-binding"]')]
        positions=positions[0:len(positions)-3]
        Wd.back()
        time.sleep(2)
    Wd.quit()
teams = ['chennai-super-kings', 'delhi-capitals', 'gujarat-titans', 'kolkata-knight-riders', 'lucknow-super-giants', 'mumbai-indians', 'punjab-kings', 'rajasthan-royals', 'royal-challengers-bangalore', 'sunrisers-hyderabad']
teamsacr = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
teams=[i.replace("-"," ") for i in teams]
teamsacr_before2022=['CSK','DC','KKR','MI','PBKS','RR','RCB','SRH']
year=int(input())
team_acr=input().upper()
dic=dict(zip(teamsacr,teams))
team=dic[team_acr]

player_pos(year,team,team_acr)
