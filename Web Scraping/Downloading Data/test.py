from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from time import sleep
import platform
import datetime
import math 

def channelDateSelector():
    # Click the arrow button which opens the channel and date selector panel
    channelSelectorBtn = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_iconShowEntitySelection')
    channelSelectorBtn.click()
    return

def dateSelector(year, isFirstHalf):
    # Enter the required dates
    dateSelectorStart = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_ctrlDatePicker_txtStartDate')
    dateSelectorEnd = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_ctrlDatePicker_txtEndDate')

    if isFirstHalf is True:
    # Formatting the dates
        startDate = str(year) + "-" + str(1) + "-" + "01" + " 00:00"
        endDate = str(year) + "-" + str(7) + "-" + "02" + " 00:00"
    else:
        startDate = str(year) + "-" + str(7) + "-" + "01" + " 00:00"
        endDate = str(year+1) + "-" + str(1) + "-" + "02" + " 00:00"


    dateSelectorStart.send_keys(Keys.CONTROL, "a")
    dateSelectorStart.send_keys(startDate)
    dateSelectorStart.send_keys(Keys.ENTER)
    dateSelectorEnd.send_keys(Keys.CONTROL, "a")
    dateSelectorEnd.send_keys(endDate)
    dateSelectorEnd.send_keys(Keys.ENTER)
    
    return

def channelSelector(channelIterator):
# Ensures that all checkboxes are un-ticked
    # print("start of channel selector")
    tickAllToggleButton = driver.find_element_by_id('ctl00_ContentPlaceHolder_Body_ctrlEntitySelector_grdEntities_DXSelAllBtn0_D')
    sleep(1)
    tickAllToggleButton.click()
    
    WebDriverWait(driver, 10).until(expected_conditions.staleness_of(tickAllToggleButton)) 
    # print('after wait')
    tickAllToggleButton2 = driver.find_element_by_id('ctl00_ContentPlaceHolder_Body_ctrlEntitySelector_grdEntities_DXSelAllBtn0_D')
    tickAllToggleButton2.click()
    
    WebDriverWait(driver, 10).until(expected_conditions.staleness_of(tickAllToggleButton2)) 
    for checkBox in channelIterator:
        
        channelSelectorCheckBox = driver.find_element_by_id('ctl00_ContentPlaceHolder_Body_ctrlEntitySelector_grdEntities_DXSelBtn' + str(checkBox) + '_D')
        # To check whether the selected checkbox is already checked
        isTickedText = channelSelectorCheckBox.get_attribute("class")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of(channelSelectorCheckBox))  
        c = isTickedText.count("Unchecked")
        if c >0:
            channelSelectorCheckBox.click()
    return

def channelRangeDeterminer(rangeNr):
    # determines first and last checkbox in the required range
    firstBox = (rangeNr-1)*25
    lastBox = rangeNr*25 
    channelRange = range(firstBox, lastBox)
    print(channelRange)
    return channelRange

def viewDataButton():
    # Click the view button
    viewDataButtonVar = driver.find_element_by_id('ContentPlaceHolder_Body_btnView')
    viewDataButtonVar.click()
    # print('view clicked')
    
    WebDriverWait(driver, 150).until(expected_conditions.staleness_of(viewDataButtonVar)) 
    return

def exportDataButton():
    # Click the export button
    # This sleep is required such that the error: "Other element would receive click" does not happen
    exportDataButtonVar = driver.find_element_by_id('ContentPlaceHolder_Body_btnExportData')
    exportDataButtonVar.click()
    # print('export clicked')
    sleep(1)
    return

# def loopDateGetter(prevMax):
#     # Define the dates to be downloaded
#     year = range(2013,2018)
#     month = range(1,12)
#     day = 1
#     return

def nextChannelSet():
    # Click the arrow button which opens the channel and date selector panel then go to the next page of meters

    # channelSelectorBtn = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_iconShowEntitySelection')
    # channelSelectorBtn.click()

    # driver.get_screenshot_as_file("channelselectorbtn.png")
    sleep(2)
    nextChannelsButton = driver.find_element_by_class_name('dxWeb_pNext_DevEx')
    nextChannelsButton.click()
    WebDriverWait(driver, 10).until(expected_conditions.staleness_of(nextChannelsButton)) 
    return

def chromeRun():
    url = "https://www.ecwin.co.za/ecWIN/wits/Login"
    # Find the operating system
    operatingSystem = platform.system()
    if operatingSystem is 'Windows':
        chromePath = "./Chrome_Driver/Windows/chromedriver.exe"
    if operatingSystem is "Mac":
        chromePath = "./Chrome_Driver/Mac/chromedriver"
    if operatingSystem is "Linux":
        chromePath = "./Chrome_Driver/Linux/chromedriver"

    # Run Chrome Headless
    chromeOptions = Options()
    # chromeOptions.add_argument("--headless")
    # chromeOptions.add_argument("--window-size=1920x1080")

    # chrome_options.add_argument


    global driver
    driver = webdriver.Chrome(chrome_options=chromeOptions, executable_path=chromePath)
    # driver.implicitly_wait(30)
    
    WebDriverWait(driver, 30).until(expected_conditions.number_of_windows_to_be(1)) 
    driver.maximize_window()

    # sleep(2)
    # Proxy Settings
   # driver.switchTo().alert().sendKeys("\788579");


    # actions = ActionChains(driver)
    # actions.send_keys("ISTpassword\788579")
    # actions.send_keys(Keys.TAB)
    # actions.send_keys("CNSPass5110")
    # actions.send_keys(Keys.TAB)
    # actions.send_keys(Keys.ENTER)

    driver.get(url)
    return

def userLogin():
    # User Details
    usernameField = driver.find_element_by_id('ContentPlaceHolder_Body_txtUsername')
    passwordField = driver.find_element_by_id('ContentPlaceHolder_Body_txtPassword')

    usernameField.send_keys("ISTPassword")
    passwordField.send_keys("ISTPassword")

    loginButton = driver.find_element_by_id('ContentPlaceHolder_Body_btnhdnLogin')
    loginButton.click()

    # Enter new url once logged in that redirects to the data editor
    # https://www.ecwin.co.za/ecWIN/wits/7.0.12.1/MODULES/REPORT/aspx/ReportViewer.aspx
    dataEditorUrl = "https://www.ecwin.co.za/ecWIN/wits/7.0.12.1/MODULES/DATAEDITOR/aspx/DataEditor.aspx"
    driver.get(dataEditorUrl)
    return

def selectDecimalPlaces():
    decimalPlaces = driver.find_element_by_xpath("//button[@data-id='ContentPlaceHolder_Body_ddlDecimalPlaces']")

    decimalPlaces.click()

    actionsTab = ActionChains(driver)
    actionsTab.send_keys(Keys.TAB)
    actionsTab.perform()
    actionsTab.perform()

    actionsEnter = ActionChains(driver)
    actionsEnter.send_keys(Keys.ENTER)
    actionsEnter.perform()

    
    sleep(2)
    return

#Main
chromeRun() # Opens chrome



userLogin() # Logs into ecWin site, goes to data editor site
selectDecimalPlaces() # select number of decimal places (#.####)
channelDateSelector()  # Clicks button to open side panel
totCheckBoxes = 623
totNrRanges = math.ceil(totCheckBoxes/25)
# totNrRanges = 2
currentYear = datetime.datetime.now().year
# Define date range variables
yearRange = range(2013, currentYear+1)

nextChannelSet()
nextChannelSet()
nextChannelSet()
nextChannelSet()
nextChannelSet()

# for checkBoxRange in range(1, totNrRanges+1):
for checkBoxRange in range(23, totNrRanges+1):
    if (checkBoxRange-1)%4 is 0:
        if checkBoxRange != 1:
            nextChannelSet() # goes to next page of check boxes
            # print('NextPage')

    channelIter = channelRangeDeterminer(checkBoxRange) # determines the numbers for the checkboxes in that range
    channelSelector(channelIter) # selects the checkboxes in the given range
    
    for year in yearRange:
        dateSelector(year, True) # selects first 6 months in the year
        viewDataButton() # clicks the view data button
        exportDataButton()
        # Need: reset button (for explicit wait)
        channelDateSelector() # open side panel
        
        dateSelector(year, False) # selects last 6 months in the year 
        viewDataButton() # clicks the view data button
        exportDataButton()
        # Need: reset button (for explicit wait)
        channelDateSelector() # open side panel

    # viewDataButton() # clicks the view data button
    # exportDataButton()
    # # Need: reset button (for explicit wait)
    # channelDateSelector() # open side panel
  


# Loop channel selection
    # Loop date selection

#for year in yearRange:
 #   dateSelector(year, True) # selects first 6 months in the year
   
  #  dateSelector(year, False) # selects last 6 months in the year 
    





# Two methods: 
    # 1: Loop through the dates for the first few selected channels, then loop through the next channels and the next dates
    # 2: Loop through the channels for a date range, then go onto the next date range.
    # I believe that 1. will be faster because it does not have to refresh the checkboxes panel and does not have to click the next page of channels button that often.


# The order of things:
    # 1. channelDateSelector()
    # 2. dateSelector()
    # 3. channelSelector()
    # 4. viewDataButton()
    # 5. exportDataButton()
    # 6. Loop



driver.quit()


# make sure that it does not loop through the dates once it gets to the current date. 
# Make sure that the already downloaded checkboxes have been unticked when all of their data has been downloaded



# Used to run the old function
# # Run function
# for i in year:
#     for j in month:
#         dateSelector(i, j,prevMax)


# Used to loop through the pages and change the bounds for which checkboxes to select 
# prevMax = 0
# for meterpages in range(7):
#     loopDateGetter(prevMax)

#     prevMax = prevMax + 100
