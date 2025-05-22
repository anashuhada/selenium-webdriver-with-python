import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# click on link
driver.find_element(By.XPATH, "//div[@id='PageList1']//ul//li//a[contains(text(),'AJAX')]").click()
driver.find_element(By.LINK_TEXT, "Download Files").click()

# find number of links in a page
links = driver.find_elements(By.XPATH, "//div[@id='PageList1']//ul//li//a")
print("Total number of links:", len(links))

# print all the link names
for link in links:
    print(link.text)

time.sleep(5)