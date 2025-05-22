# install requests package through file > settings > project interpreter

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.XPATH, "//ul//li//a")
count = 0
for link in all_links:
    url = link.get_attribute('href')

    try:
        response_req = requests.head(url)
    except:
        None

    if response_req.status_code >= 400:
        print(url, " is broken link")
        count += 1
    else:
        print(url, " is valid link")

print("Total number of broken links: ", count)