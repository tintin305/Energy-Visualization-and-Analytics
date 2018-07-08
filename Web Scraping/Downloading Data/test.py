from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from time import sleep

# Function definition
def editorLooper(i, j,prevMax):

    # Click the arrow button which opens the channel and date selector panel
    channelSelectorBtn = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_iconShowEntitySelection')
    channelSelectorBtn.click()
    driver.get_screenshot_as_file("channelselectorbtn.png")

    # Enter the required dates
    dateSelectorStart = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_ctrlDatePicker_txtStartDate')
    dateSelectorEnd = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_ctrlDatePicker_txtEndDate')

    # Formatting the dates
    startDate = str(i) + "-" + str(j) + "-" + "01" + " 00:00"
    endDate = str(i) + "-" + str(j+1) + "-" + "01" + " 00:00"
    
    dateSelectorStart.send_keys(Keys.CONTROL, "a")
    dateSelectorStart.send_keys(startDate)
    dateSelectorStart.send_keys(Keys.ENTER)
    dateSelectorEnd.send_keys(Keys.CONTROL, "a")
    dateSelectorEnd.send_keys(endDate)
    dateSelectorEnd.send_keys(Keys.ENTER)

    driver.get_screenshot_as_file("date.png")

    # Select the required channel
    if prevMax >= 600:
        meterLimiter = 30
    else:
        meterLimiter = 99
    channelIterator = range(prevMax+0,prevMax+meterLimiter)
    for checkBox in channelIterator:
        channelSelectorCheckBox = driver.find_element_by_id('ctl00_ContentPlaceHolder_Body_ctrlEntitySelector_grdEntities_DXSelBtn' + str(checkBox) + '_D')
        # To check whether the selected checkbox is already checked
        tickAllToggleButton = driver.find_element_by_id('ctl00_ContentPlaceHolder_Body_ctrlEntitySelector_grdEntities_DXSelAllBtn0_D')
        tickAllToggleButton.click()
        tickAllToggleButton.click()
        isTickedText = channelSelectorCheckBox.get_attribute("class")
        isCheckedTest = "dxWeb_edtCheckBoxChecked_DevEx dxICheckBox_DevEx dxichSys"
        if isTickedText != isCheckedTest:
            channelSelectorCheckBox.click()


    # Click the view button
    viewButton = driver.find_element_by_id('ContentPlaceHolder_Body_btnView')
    driver.get_screenshot_as_file("channelselectorbtn.png")
    viewButton.click()
    driver.get_screenshot_as_file("view.png")

    # Click the export button
    # This sleep is required such that the error: "Other element would receive click" does not happen
    sleep(15)
    exportButton = driver.find_element_by_id('ContentPlaceHolder_Body_btnExportData')
    exportButton.click()

    driver.get_screenshot_as_file("export.png")
    prevMax = prevMax + 100
    return

def loopDateGetter(prevMax):
    # Define the dates to be downloaded
    year = range(2013,2018)
    month = range(1,12)
    day = 1


    # Run function
    for i in year:
        for j in month:
            editorLooper(i, j,prevMax)


    # Click the arrow button which opens the channel and date selector panel then go to the next page of meters
    channelSelectorBtn = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_iconShowEntitySelection')
    channelSelectorBtn.click()
    driver.get_screenshot_as_file("channelselectorbtn.png")
    nextChannelsButton = driver.find_element_by_class_name('dxWeb_pNext_DevEx')
    nextChannelsButton.click()

    return


url = "https://www.ecwin.co.za/ecWIN/wits/Login"

chrome_options = Options()
# Run Chrome Headless
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(30)
driver.maximize_window()
driver.get(url)


# User Details
usernameField = driver.find_element_by_id('ContentPlaceHolder_Body_txtUsername')
passwordField = driver.find_element_by_id('ContentPlaceHolder_Body_txtPassword')

usernameField.send_keys("ISTPassword")
passwordField.send_keys("ISTPassword")

loginButton = driver.find_element_by_id('ContentPlaceHolder_Body_btnhdnLogin')
loginButton.click()


driver.get_screenshot_as_file("login.png")

# Enter new url once logged in that redirects to the data editor
dataEditorUrl = "https://www.ecwin.co.za/ecWIN/wits/7.0.12.1/MODULES/DATAEDITOR/aspx/DataEditor.aspx"
driver.get(dataEditorUrl)

driver.get_screenshot_as_file("editor.png")

prevMax = 0
for meterpages in range(7):
    loopDateGetter(prevMax)

driver.quit()


# make sure that it does not loop through the dates once it gets to the current date. 
# Make sure that the already downloaded checkboxes have been unticked when all of their data has been downloaded