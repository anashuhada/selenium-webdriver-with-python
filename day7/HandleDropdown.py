import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drop_country = driver.find_element(By.XPATH, "//select[@id='country']")
country = Select(drop_country)

# select option from the dropdown
country.select_by_visible_text("Japan")
country.select_by_value("uk")
country.select_by_index(5)

# capture all the options and print them using built-in function
option_country = country.options
print("Total countries:", len(option_country))
for op in option_country:
    print(op.text)

# without built-in function
option_country = country.options
for op in option_country:
    if op.text == "Japan":
        op.click()
        break

# directly use the xpath
list_country = driver.find_elements(By.XPATH, "//select[@id='country']//option")
print(len(list_country))

for ls in list_country:
    if ls.text == "Japan":
        ls.click()
        break

time.sleep(5)