import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
country_list = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']//li")
print(len(country_list))

for country in country_list:
    if country.text == "Malaysia":
        print(country.text)
        country.click()
        break

time.sleep(5)