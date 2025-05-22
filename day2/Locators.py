import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, "name").send_keys("Tyeso")

# email_text = driver.find_element(By.LINK_TEXT, "Email:")
# print(email_text.is_displayed())

checkboxes = driver.find_elements(By.XPATH, "//div[@class='form-group']//label[@class='form-check-label']")
(print(len(checkboxes)))

for ch in checkboxes:
        print(ch.text)

time.sleep(5)