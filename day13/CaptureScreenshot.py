import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

time.sleep(5)

# driver.save_screenshot("/Users/anashuhada/PycharmProjects/SeleniumWithPython/day13/screenshot.png")
driver.save_screenshot(os.getcwd() + "/capture_screenshot.png")
driver.get_screenshot_as_file(os.getcwd() + "/capture_screenshot.png")
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64() these 2 save in binary format
driver.quit()