from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json, time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def finds(x , TAG = False, multiple = False, parent = None ,t = 5):
    try:
        if not TAG:
            WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.XPATH, x)))
            if parent == None:
                if not multiple: return driver.find_element(By.XPATH, x)
                else: return driver.find_elements(By.XPATH, x)
            else:
                if not multiple: return driver.find_element(By.XPATH, x)
                else: return parent.find_elements(By.XPATH, x)
        else:
            WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.TAG_NAME, x)))
            if parent == None:
                if not multiple: return driver.find_element(By.TAG_NAME, x)
                else: return driver.find_elements(By.TAG_NAME, x)
            else:
                if not multiple: return driver.find_element(By.TAG_NAME, x)
                else: return parent.find_elements(By.TAG_NAME, x)
    except Exception:
        return None
    
#settup

    #staring link


    #getComapnyNames
filteredNamed = []
with open("./insider-trading/comapnyData.json",'r') as file:
    rawNames = json.load(file)
for item in rawNames:
    if item[2]:
        filteredNamed.append(item[1])
    else: pass

#starting

    #start driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#running

    #goto companies
for company in filteredNamed:
        #refine company name
    company.replace(" ", "+")
        #goto refined link
    driver.get(f"https://www.sec.gov/cgi-bin/srch-edgar?text=%28{company}%29&first=2000&last=2023")
        #wait
    time.sleep(1)
#ending

driver.quit()
