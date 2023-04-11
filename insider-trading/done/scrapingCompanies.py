from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json, time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = 'https://en.wikipedia.org/wiki/List_of_largest_oil_and_gas_companies_by_revenue'
driver.get(link)

time.sleep(1)
table = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody')
rows = table.find_elements(By.TAG_NAME, "tr")

rowData = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    collumData = []
    for col in cols:
        collumData.append(col.text)
    rowData.append(collumData)

driver.quit()

with open("./insider-trading/comapnyData.json", "w") as file:
    json.dump(rowData, file)