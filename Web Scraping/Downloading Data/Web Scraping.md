---
title: Web Scraping
---

# The Main Problem

As described in the beginning of [this](https://www.youtube.com/watch?v=UrsUuVAJh5U) video, is that the data is not in the source, it is in the browser, and the reason why is that it only exists in Javascript. When you inspect the element you are able to see the data inside the table, however you can't see it in the source. This is why BeautifulSoup can't be used alone, this is why we are going to be using Python Requests.
You can use Selenium, however it is slow.

When looking at the Network, you are interested in looking at the POST methods.
When you select the POST that appears to have the required information, you can see all kinds of information about it.
If you select the "Response" tab of this post, you will see the data that is sent to the browser. In this case, the information is encrypted, so it is not human readable and not easy to find in the POST response.
The Fiddler tool can make these requests without using Python just yet, this allows you to see the data come back for viewing.
When copying the POST command from the Network viewer into the Fiddler tool and pasting it into the Composer > Parsed > and the paste it into the url space, select POST as the method. In the request body, go back to the Network viewer, and under the headers tab, find the Form Data, and view the source (you want the raw data), paste this into the request body.
Then click execute in Fiddler.
This process would normally get the required result, however, the response from the host was that a login is required, so this will require some more work.

# Beautiful Soup

## Install

Install Python 3.6 (keep consistent)
Install Anaconda
Test out anaconda by going to the command line and typing: python
You should see three >'s appear, this tells you that you are in the python environment.
The next step is to install beautiful soup.
Do this by:

- Go into cmd
- Enter "pip install bs4"
- You will know that it is installed if you enter the python environment, enter "import bs4" and if you get no errors, you know it has been installed.

Next you need a web client to grab stuff from the internet. You can use a package: "url lib" inside this package is a module called "request" and in that is a function called "url open".

- Useful way to parse HTML text

````python
import bs4
from urllib.request import urlopen as uReq # Saving time
from bs4 import BeautifulSoup as soup # This is to make it easier to refer to the importing of BeautifulSoup
my_url = 'https://www.ecwin.co.za/ecWIN/wits/'
# Calling url open over here:
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
````

This has its shortfalls as it cannot interact with the web page once the page has loaded.

It seems that there may be a way to select links using beautiful soup, however mostly Selenium is used for this.

# Selenium

This will interact with a web page. It is difficult to get it to work headless. This means that it physically launches a web browser and does all of the operations, this is tedius.

I have managed to get a useful system working for this package. I managed to get it to "look" better. This means that I launch a headless version of Chrome which does all of the same steps as above.
I believe that Selenium may be the best out of the following packages based on its user base...
I managed to get the headless version working by following [this](https://medium.com/@pyzzled/running-headless-chrome-with-selenium-in-python-3f42d1f5ff1d) guide.

From what I can see, only the chrome browser allows headless mode (out of the major web browsers). There are other web browsers, ones that run alongside python that are natively headless (PhantomJS, SlimerJS, TrifleJS, Nightmare), however I cannot speak to their functionality other than the fact that I saw that PhantomJS is no longer being maintained.

Here are a few other links ([1](https://medium.com/@eliasnogueira/running-selenium-tests-with-chrome-headless-5edd624efb92), [2](https://thefriendlytester.co.uk/2017/04/new-headless-chrome-with-selenium.html), [3](https://medium.com/@pyzzled/running-headless-chrome-with-selenium-in-python-3f42d1f5ff1d)) that illustrate the process to get the system running headless (with other languages as well).

The test code that I got to work is:

````python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from time import sleep

#url = "https://www.ecwin.co.za/ecWIN/wits/Login"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(30)
driver.get("https://www.google.com")
lucky_button = driver.find_element_by_css_selector("[name=btnI]")
lucky_button.click()

driver.get_screenshot_as_file("capture.png")

sleep(2)

driver.quit()
````

This saves a screenshot of the "I am feeling lucky" page from google and saves it to the current directory.

[This](https://www.youtube.com/watch?v=UrsUuVAJh5U) dude says that it can be slow.

## Selenium with Python

[This](http://selenium-python.readthedocs.io) page has lots of info for using Selenium with Python.

[Another](https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72)

## Iteration Approach

[This](https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251) uses selenium, pandas, and BeautifulSoup to iterate through a website to gather a whole host of information.

## In Depth

[This](https://automatetheboringstuff.com/chapter11/) seems to go into quite a bit of depth, they do a few examples as well.

# Mechanize

[Looks](http://wwwsearch.sourceforge.net/mechanize/) like a small version of selenium

# PhantomJS

[This](http://phantomjs.org) is a headless browser.
Headless, and looks simple, works with selenium to do the work.

# Webbrowser (Python package)

Does not look like it can do much past loading a web page and viewing the information.

# Robobrowser

Looks to have all the functionality that is required.
[Robobrowser](http://robobrowser.readthedocs.io/en/latest/readme.html) is advertised in such a way that it will fulfill the criteria of the web scraper. It can fetch a page, click on links and buttons, and fill out and submit forms- all of these are highly important. It makes use of Requests and BeautifulSoup.
[Here](https://www.youtube.com/watch?v=hrdDIrT9kJI) is a video illustrating some of its stuff.

# Scrapy

Haven't had a look at this yet, however it looks like quite a simple tool.

# HTTrack

This [program](http://www.httrack.com/page/2/en/index.html), from what people say, can copy an entire website. It is commonly used to download a website so that it can be viewed offline. I cannot vouch for its ability. It does not look like it is maintained. I do not want to test with this as it may have the ability to damage parts of the site, which I do not want to happen.

# Requests: HTTP for Humans

[Requests](http://docs.python-requests.org/en/master/) allows you to send organic, grass-fed HTTP/1.1 requests, without the need for manual labor. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, thanks to urllib3.

# Fiddler

Seems to be useful for debugging the application, it can be used to look at requests that take place within the browser. I attemted to use Fiddler, it was capable of viewing the encrypted traffic sent by the website, when viewing the Inspectors tab, and in that the WebView tab, it was able to show the data inside the table.