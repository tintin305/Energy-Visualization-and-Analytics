from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from time import sleep

# Function definition
def editorLooper(i, j):

    # Click the arrow button which opens the channel and date selector panel
    channelSelectorBtn = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_iconShowEntitySelection')
    channelSelectorBtn.click()
    driver.get_screenshot_as_file("channelselectorbtn.png")

    # Enter the required dates
    dateSelectorStart = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_ctrlDatePicker_txtStartDate')
    dateSelectorEnd = driver.find_element_by_id('ContentPlaceHolder_Body_ctrlEntitySelector_ctrlDatePicker_txtEndDate')

    # Formatting the dates
    startDate = str(i) + "-" + str(j) + "-" + "01" + " 00:00"
    startDate = str(i) + "-" + str(j+1) + "-" + "01" + " 00:00"
    
    dateSelectorStart.send_keys(Keys.CONTROL, "a")
    dateSelectorStart.send_keys("2013-01-01 00:00")
    dateSelectorEnd.send_keys(Keys.CONTROL, "a")
    dateSelectorEnd.send_keys("2013-02-01 00:00")
    dateSelectorEnd.send_keys(Keys.ENTER)

    driver.get_screenshot_as_file("date.png")

    # Select the required channel
    channelIterator = range(0,99)
    for test in channelIterator:
        channelSelectorCheckBox = driver.find_element_by_id('ctl00_ContentPlaceHolder_Body_ctrlEntitySelector_grdEntities_DXSelBtn' + str(test) + '_D')
        channelSelectorCheckBox.click()

    # Click the view button
    viewButton = driver.find_element_by_id('ContentPlaceHolder_Body_btnView')
    viewButton.click()

    driver.get_screenshot_as_file("view.png")

    # Click the export button
    exportButton = driver.find_element_by_id('ContentPlaceHolder_Body_btnExportData')
    exportButton.click()

    driver.get_screenshot_as_file("export.png")

    sleep(2)

    driver.quit()
    return;

url = "https://www.ecwin.co.za/ecWIN/wits/Login"

chrome_options = Options()
# Run Chrome Headless
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(30)
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


# Define the dates to be downloaded
year = range(2013,2018)
month = range(1,12)
day = 1

# Run function
for i in year:
    for j in month:
        editorLooper(i, j)
