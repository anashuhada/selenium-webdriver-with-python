import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
field2 = driver.find_element(By.XPATH, "//input[@id='field2']")
button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

field1.clear()
field1.send_keys("Selenium")

act = ActionChains(driver)
act.double_click(button).perform()

print(field2.get_attribute('value'))

time.sleep(5)