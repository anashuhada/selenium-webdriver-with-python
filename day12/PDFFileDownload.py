import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

location = os.getcwd()

def chrome_setup():
    service = Service(ChromeDriverManager().install())

    # download files in desired location
    # preferences = {"download.default_directory": "/Users/anashuhada/PycharmProjects/SeleniumWithPython/day12"}
    preferences = {"download.default_directory": location,
                   "plugins.always_open_pdf_externally": True
                   } # save files in desired location
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", preferences) # desired location

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def edge_setup():
    service = Service(EdgeChromiumDriverManager().install())

    preferences = {"download.default_directory": location,
                   "plugins.always_open_pdf_externally": True
                  } # save files in desired location
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option("prefs", preferences) # desired location

    driver = webdriver.Edge(service=service, options=edge_options)
    return driver

def firefox_setup():
    service = Service(GeckoDriverManager().install())

    # settings
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    firefox_options.set_preference("browser.download.manager.showWhenStarting", False) # download browser won't appear
    # https://www.sitepoint.com/mime-types-complete-list/
    firefox_options.set_preference("browser.download.folderList", 2) # 0 = download in desktop, 1 = in default loc, 2 = desired loc
    firefox_options.set_preference("browser.download.dir", location)
    firefox_options.set_preference("pdfjs.disabled", True) # for pdf
    driver = webdriver.Edge(service=service, options=firefox_options)
    return driver

driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

time.sleep(5)