from selenium import webdriver                                      
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json, time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import datetime as DT
import dateutil.relativedelta

# pre-starting
sleepDur = 10

# user work needed

pswrdData = 'Millwood45'
plantData = ['US8X', 'US8Y']
week = False
month = True
year = False

#work done
userData = 'PL_FACTORS'

# dates
today = date.today()
#week before
weekAgo = today - DT.timedelta(days=7)
#month before
monthAgo = today + dateutil.relativedelta.relativedelta(months=-1)
# year before
yearAgo = today - dateutil.relativedelta.relativedelta(years=1)

### AUTH ###
# start driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# goto link
baselink = "https://esp.chep.com/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html"
driver.get(baselink)

# get user / pswrd
WebDriverWait(driver, sleepDur).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="PASSWORD_FIELD-inner"]')))
userFeild = driver.find_element(By.XPATH, '//*[@id="USERNAME_FIELD-inner"]')
pswrdFeild = driver.find_element(By.XPATH, '//*[@id="PASSWORD_FIELD-inner"]')

# input user / pswrd
userFeild.send_keys(userData)
pswrdFeild.send_keys(pswrdData, Keys.ENTER)


# iterate through plants
for plant in plantData:

    ### create link ###

    plantCode = plant

    if week:
        startDate = weekAgo
    elif month:
        startDate = monthAgo
    elif year:
        startDate = yearAgo

    endDate = today

    # goto reports PG
    finalLink = f'https://esp.chep.com/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html?sap-client=600&sap-language=EN#ZESP_USREPORTS-display&/TowerReport/TOWER%20REPORT/{plantCode}/{str(startDate)},{endDate}/00:00:00/23:59:59'
    driver.get(finalLink)

    #download 
    time.sleep(1)
    waitElement = driver.find_element(By.XPATH, '//*[@id="sapUiBusyIndicator"]')
    WebDriverWait(driver, 1000).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="sapUiBusyIndicator"]')))

    exportBtn = driver.find_element(By.XPATH, '//*[@id="__jsview26--Export-inner"]')
    exportBtn.click()
    

# end driver
driver.quit()