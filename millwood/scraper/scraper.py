from selenium import webdriver                                      
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json, time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date

# pre-starting
sleepDur = 10
userData = 'PL_FACTORS'
pswrdData = 'Millwood45'
plantData = ['US8X', 'US8Y']
today = date.today()
todaySparced = str(today).split('-')
year = int(todaySparced[0])
month = int(todaySparced[1])
day = int(todaySparced[2])
monthList = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
currentMonth = monthList[month-1]


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

    # goto reports PG
    reportLink = 'https://esp.chep.com/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html?sap-client=600&sap-language=EN#ZESP_USREPORTS-display'
    driver.get(reportLink)

    # get report Feild
    time.sleep(3)
    reportFeild = driver.find_element(By.XPATH, '//*[@id="__jsview26--onRepSelect"]')
    reportFeild.click()

    # select tower from report
    WebDriverWait(driver, sleepDur).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__item2-__jsview26--onRepSelect-3"]')))
    towerSelect = driver.find_element(By.XPATH, '//*[@id="__item2-__jsview26--onRepSelect-3"]')
    towerSelect.click()

    # open plant code
    WebDriverWait(driver, sleepDur).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__jsview26--mPlant__vhi"]')))
    plantBtn = driver.find_element(By.XPATH, '//*[@id="__jsview26--mPlant__vhi"]')
    plantBtn.click()

    # input plant code search
    WebDriverWait(driver, sleepDur).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="searchFiledId-I"]')))
    plantEntry = driver.find_element(By.XPATH, '//*[@id="searchFiledId-I"]')
    plantEntry.send_keys(plant, Keys.ENTER)

    # get result body
    plantResultBody = driver.find_element(By.XPATH, '//*[@id="plantName-tblBody"]')
    # select result
    plantResultTr = plantResultBody.find_element(By.TAG_NAME, 'tr')
    plantResultTr.click()
    # select accept
    plantAccept = driver.find_element(By.XPATH, '//*[@id="accept"]')
    plantAccept.click()
    
    #skip dates?
    skipDates = True

    if not skipDates:
        # open start date
        startDateEntry = driver.find_element(By.XPATH, '//*[@id="__jsview26--DataFrom-icon"]')
        startDateEntry.click()

        # get month btn
        startMonthBtn = driver.find_element(By.XPATH, '//*[@id="__jsview26--DataFrom-cal--Head-B1"]' )

        # see if months match
        if not currentMonth ==  startMonthBtn.text:
            # open month selection
            startMonthBtn.click()
            # get conatiner for months
            startMonthCon = driver.find_element(By.XPATH, '//*[@id="__jsview26--DataFrom-cal--MP"]')
            # get rows in container
            startMonthRows = startMonthCon.find_elements(By.TAG_NAME, 'div')
            # iterate through rows
            for row in startMonthRows:
                # get cols from row
                startMonthCols = row.find_elements(By.TAG_NAME, 'div')
                for col in startMonthCols:
                    #check if match
                    if col.text is currentMonth:
                        col.click()
                        break
        else: pass

        # get container of rows
        startDayCon = driver.find_element(By.XPATH, '//*[@id="__jsview26--DataFrom-cal--Month0-days"]')
        # get the rows inside of container
        startDayRows = startDayCon.find_elements(By.TAG_NAME, 'div')
        #iterate through rows
        for row in startDayRows:
            # get cols in rows
            startMonthCols = ''
            ##### TODO #####
            # fix date selection
            ################
    # open end date

    # submit
    submitBtn = driver.find_element(By.XPATH, '//*[@id="__button10-content"]')
    submitBtn.click()

time.sleep(10000)

# end driver
driver.quit()