import csv 
import undetected_chromedriver as uc
import ssl
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
ssl._create_default_https_context = ssl._create_unverified_context
from selenium.webdriver.common.action_chains import ActionChains   


options = ChromeOptions()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
PATH='./chromedriver.exe'

website = 'https://www.iplt20.com/'

ser = Service(PATH)
wd = webdriver.Chrome(options = options, service=ser)
#wd.get(website)
#wd.maximize_window()
#time.sleep(5)

def getpoints():
      website_points = 'https://fantasy.iplt20.com/'
      dri2 = webdriver.Chrome(options=options, service=ser)
      dri2.get(website_points)
      dri2.maximize_window()
      WebDriverWait(dri2, 5).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div/a[2]')))
      dri2.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div/a[2]').click()
      WebDriverWait(dri2, 25).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/ul/li[1]/div')))
      dri2.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]/div[2]/ul/li[1]/div').click()
      time.sleep(5)
      for j in range(4):
        if j==1:
            dri2.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div[1]/div[1]/div[6]/ul/li[2]/span').click()
            WebDriverWait(dri2, 2).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class = "df-plyrSel__name"]')))
        if j==2:
            dri2.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div[1]/div[1]/div[6]/ul/li[3]/span').click()
            WebDriverWait(dri2, 2).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class = "df-plyrSel__name"]')))
        if j==3:
            dri2.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div[1]/div[1]/div[6]/ul/li[4]/span').click()
            WebDriverWait(dri2, 2).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class = "df-plyrSel__name"]')))
        pl_names = [i.text for i in dri2.find_elements(By.XPATH, '//div[@class = "df-plyrSel__name"]')]
        pl_points = [i.text for i in dri2.find_elements(By.XPATH, '//div[@class = "df-tbl__cell df-tbl__cell--pts"]')]
        pl_credits = [i.text for i in dri2.find_elements(By.XPATH, '//div[@class = "df-tbl__cell df-tbl__cell--amt"]')]
        pl_cred_info = list(zip(pl_names,pl_points,pl_credits))
        with open('player_points_info.csv', 'w') as o2:
            csv_o2 = csv.writer(o2)
            csv_o2.writerow(['player_name','player_points', 'player_credits'])
            for k in range(len(pl_names)):
                csv_o2.writerow(pl_cred_info[k])

      #print()
getpoints()
'''
WebDriverWait(wd, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#myHeader > div > div.site-navbar-wrap > div > div > nav > ul > li:nth-child(5) > a")))
wd.find_element(By.CSS_SELECTOR, '#myHeader > div > div.site-navbar-wrap > div > div > nav > ul > li:nth-child(5) > a').click()
teams = ['chennai-super-kings', 'delhi-capitals', 'gujarat-titans', 'kolkata-knight-riders', 'lucknow-super-giants', 'mumbai-indians', 'punjab-kings', 'rajasthan-royals', 'royal-challengers-bangalore', 'sunrisers-hyderabad']
teamsacr = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']

time.sleep(5)



for i in range(10):
    k=100
    if (i>=4):
            wd.execute_script("window.scrollTo(0, 520);")
            time.sleep(2)
    element=wd.find_element(By.XPATH,f'//a[@href="https://www.iplt20.com/teams/{teams[i]}"]')
    element.click()
    time.sleep(2)
    
    player_name = [j.text for j in wd.find_elements(By.XPATH, '//div[@class="ih-p-name"]')]
    player_id = [f'{teamsacr[i]}{k+j}' for j in range(len(player_name))]
    player_role = [j.text for j in wd.find_elements(By.XPATH, '//span[@class="d-block w-100 text-center"]')]
    player_infoAll = list(zip(player_id, player_name, player_role))


    with open (f'../2023/{teamsacr[i]}.csv', 'w') as out:
          csv_out=csv.writer(out)
          csv_out.writerow(['player_id','player_name', 'player_role'])
          for l in range(len(player_name)):
                csv_out.writerow(player_infoAll[l])

    wd.back()
    time.sleep(2) 
'''

      

#pdetails = {}


wd.quit()


