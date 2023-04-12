from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json, time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.govtrack.us/congress/members/current")

WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[2]/section/div/div[2]')))
body = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/section/div/div[2]')

As = driver.find_elements(By.TAG_NAME, "a")
trDATA = []
for a in As:
    trDATA.append(a.get_attribute('href'))
print(trDATA)

driver.quit()

with open("./insider-trading/congressNames.json", "w" ) as file:
    json.dump(trDATA, file)