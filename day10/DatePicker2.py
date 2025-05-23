import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# date of birth
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='dob']").click()

time.sleep(3)
datepicker_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("May")
datepicker_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("2020")
date_element = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tr//td")
for dt in date_element:
    if dt.text == "30":
        dt.click()
        print(datepicker_month, dt.text, datepicker_year)
        break

time.sleep(5)