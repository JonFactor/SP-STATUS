from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json, time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

filteredNamed = []
with open("./insider-trading/comapnyData.json",'r') as file:
    rawNames = json.load(file)
for item in rawNames:
    if item[1] and  len(item[1]) >= 20:
        filteredNamed.append(item[1][:20])
    elif item[1] and len(item[1]) >= 4:
        filteredNamed.append(item[1])
    else: pass

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://www.sec.gov/edgar/searchedgar/cik"

count = 0
CIKs = []
try:
    for name in filteredNamed:
        while True:
            driver.get(link)
            WebDriverWait(driver, .3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="company"]')))
            entry = driver.find_element(By.XPATH, '//*[@id="company"]')
            try:
                entry.send_keys(name, Keys.ENTER)
                try:
                    WebDriverWait(driver, .3).until(EC.visibility_of_element_located((By.XPATH, "/html/body/table/tbody/tr/td[2]/p[1]/strong")))
                    results = driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/p[1]/strong")
                    if results.text == '0':
                        break
                    elif results.text == '1':
                        WebDriverWait(driver, .3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/table/tbody/tr/td[2]/pre[2]/a')))
                        CIK = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[2]/pre[2]/a')
                        CIKtxt = CIK.text
                        CIKs.append([CIKtxt])
                        break
                    elif results.text >= '2' and results.text <= '15':
                        pre = driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/pre[2]")
                        aS = pre.find_elements(By.TAG_NAME, 'a')
                        aSlist = []
                        for a in aS:
                            aSlist.append(a.text)
                        CIKs.append(aSlist)
                        break
                    else:
                        break
                except Exception:
                    pass
            except Exception:
                count += 1
                pass
except KeyboardInterrupt:
    pass
driver.quit()

print(CIKs, count)

with open("./insider-trading/companyCIKs.json", "w") as file:
    json.dump(CIKs, file)