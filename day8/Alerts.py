import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# open alert window
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alert_window = driver.switch_to.alert
print("Text:", alert_window.text)
alert_window.send_keys("Selenium with Python")
alert_window.accept()
time.sleep(5)