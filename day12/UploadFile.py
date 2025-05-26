import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://practice.expandtesting.com/upload")
driver.maximize_window()

time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='fileInput']").send_keys("/Volumes/KINGSTON/FileToUpload1.txt")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@id='fileSubmit']").submit()
time.sleep(5)