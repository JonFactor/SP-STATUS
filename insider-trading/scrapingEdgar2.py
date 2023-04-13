from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json, time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

companies = ['Apple Inc.', 'Microsoft Corp']

compainyData = []
for company in companies:
    driver.get(f"https://www.sec.gov/cgi-bin/srch-edgar?text=%28{company}%29")
    pageData = []
    while True:
        time.sleep(.3)
        try:
            table = driver.find_element(By.XPATH, '/html/body/div/table/tbody')
        except Exception:
            continue
        trs = table.find_elements(By.TAG_NAME, 'tr')

        trDATA = []
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME, 'td')
            if len(tds) <= 0:
                continue
            nameContain = tds[1]
            name = nameContain.find_element(By.TAG_NAME, 'a')
            if company not in str(name.text):
                print(name.text)
                continue
            contentContain = tds[2]
            links = contentContain.find_elements(By.TAG_NAME, 'a')
            text = links[0]
            if text.get_attribute('href') in trDATA:
                break
            trDATA.append(text.get_attribute('href'))
        pageData.append(trDATA)
        try:
            driver.find_element(By.XPATH, '/html/body/div/center[1]/a[2]').click()
        except Exception:
            break
    compainyData.append(pageData)
driver.quit()