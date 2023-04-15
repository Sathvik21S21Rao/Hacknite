from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time,csv
def batting_stats(year,team,team_acr):
    PATH="/usr/bin/chromedriver.exe"
    ser=Service(PATH)
    Wd=webdriver.Chrome(service=ser)
    Wd.maximize_window()
    Wd.get(f"https://www.iplt20.com/stats/{year}")
    time.sleep(2)
    menu=Wd.find_elements(By.XPATH,"//div[@class='cSBDisplay ng-binding']")[2]
    Wd.execute_script("window.scrollTo(0,300);")
    time.sleep(2)
    menu.click()
    time.sleep(2)
    L=Wd.find_elements(By.XPATH,'//div[@class="cSBList active"]/div')
    pos=0
    for j in range(len(L)):
        if team_acr==L[j].text.strip():
            pos=j
            break
    details="Player Mat	Inns NO	Runs HS	Avg	BF SR 100 50 4s	6s"
    try:
        L[pos].click()
        time.sleep(2)
    except:
        ActionChains(Wd).move_to_element(L[0]).perform()
        Wd.execute_script("arguments[0].scrollIntoView();",menu)
        L[pos].click()
        time.sleep()
    #ActionChains(Wd).move_to_element(L[pos+1]).click()
    player_names=[i.text for i in Wd.find_elements(By.XPATH,"//div[@class='st-ply-name ng-binding']")]
    player_stats=[]
    for j in range(len(player_names)):
        T=Wd.find_elements(By.XPATH,f"//tr[@class='{team_acr}_{j}']/td")[2:]
        player_stats.append([player_names[j]]+[i.text for i in T])
    with open(f"./{year}/{team_acr}_Batstats.csv","w") as fp:
        writer=csv.writer(fp)
        writer.writerow(details.split())
        for i in range(len(player_stats)):
            writer.writerow(player_stats[i])


def bowling_stats(year,team,team_acr):
    PATH="/usr/bin/chromedriver.exe"
    ser=Service(PATH)
    Wd=webdriver.Chrome(service=ser)
    Wd.maximize_window()
    Wd.get(f"https://www.iplt20.com/stats/{year}")
    time.sleep(2)
    menu=Wd.find_elements(By.XPATH,"//div[@class='cSBDisplay ng-binding']")[1]
    Wd.execute_script("window.scrollTo(0,300);")
    time.sleep(2)
    menu.click()
    time.sleep(2)
    Wd.find_element(By.XPATH,'//span[@class="cSBListFItems bowFItem"]').click()
    time.sleep(2)
    menu=Wd.find_elements(By.XPATH,"//div[@class='cSBDisplay ng-binding']")[1]
    Wd.find_element(By.XPATH,'//div[@class="cSBListItems bowlers ng-binding ng-scope selected"]').click()
    time.sleep(2)
    Wd.execute_script("window.scrollTo(0,300);")
    time.sleep(2)
    menu=Wd.find_elements(By.XPATH,"//div[@class='cSBDisplay ng-binding']")[2]
    menu.click()
    time.sleep(2)
    L=Wd.find_elements(By.XPATH,'//div[@class="cSBList active"]/div')
    pos=0
    for j in range(len(L)):
        if team_acr==L[j].text.strip():
            pos=j
            break
    details="Player	Mat	Inns Ov	Runs Wkts BBI Avg Econ SR 4w 5w"
    ActionChains(Wd).move_to_element(L[0]).perform()
    Wd.execute_script("arguments[0].scrollIntoView();",menu)
    #ActionChains(Wd).move_to_element(L[pos+1]).click()
    L[pos].click()
    player_names=[i.text for i in Wd.find_elements(By.XPATH,"//div[@class='st-ply-name ng-binding']")]
    player_stats=[]
    for j in range(len(player_names)):
        T=Wd.find_elements(By.XPATH,f"//tr[contains(@class,'{team_acr}_{j}')]/td")[2:]
        player_stats.append([player_names[j]]+[i.text for i in T])
    with open(f"./{year}/{team_acr}_Bowlstats.csv","w") as fp:
        writer=csv.writer(fp)
        writer.writerow(details.split())
        for i in range(len(player_stats)):
            writer.writerow(player_stats[i])
teams = ['chennai-super-kings', 'delhi-capitals', 'gujarat-titans', 'kolkata-knight-riders', 'lucknow-super-giants', 'mumbai-indians', 'punjab-kings', 'rajasthan-royals', 'royal-challengers-bangalore', 'sunrisers-hyderabad']
teamsacr = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
teams=[i.replace("-"," ") for i in teams]
teamsacr_before2022=['CSK','DC','KKR','MI','PBKS','RR','RCB','SRH']
dic=dict(zip(teamsacr,teams))
year=int(input())
if(year<2022):
    teamlist=teamsacr_before2022
else:
    teamlist=teamsacr
for i in range(len(teamlist)):
    batting_stats(year,dic[teamlist[i]],teamlist[i])
#for i in range(len(teamlist)):
    #bowling_stats(year,dic[teamlist[i]],teamlist[i])