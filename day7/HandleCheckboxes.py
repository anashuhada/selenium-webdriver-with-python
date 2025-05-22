import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# select specific checkbox
driver.find_element(By.XPATH, "//input[@id='sunday']").click()

# select all checkboxes
checkboxes = driver.find_elements(By.XPATH, "//div[@class='form-group']//input[@type='checkbox']")

# approach 1
for i in range(len(checkboxes)):
    checkboxes[i].click()

# approach 2
for ch in checkboxes:
    # print(ch.get_attribute('value'))
    ch.click()

# select multiple checkboxes by choice
for ch in checkboxes:
    day = ch.get_attribute('value')
    if day == "sunday" or day == "friday":
        ch.click()

# select last 2 checkboxes
# totalnumberofelements - 2 = starting index
for i in range(len(checkboxes) - 2, len(checkboxes)): # range(5,7) --> 6, 7
    checkboxes[i].click()

# select first 2 checkboxes
for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()

# clearing all the checkboxes
for i in range(len(checkboxes)):
    checkboxes[i].click()

time.sleep(3)

for i in range(len(checkboxes)):
    if checkboxes[i].is_selected():
        checkboxes[i].click()

time.sleep(5)