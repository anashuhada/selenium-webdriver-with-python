import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

time.sleep(3)
driver.switch_to.frame(0)

# mm/dd/yyyy
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("05/30/2025")

year = "2025"
month = "June"
date = "30"
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    curr_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    curr_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if curr_month == month and curr_year == year:
        break

    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click() # next arrow
        # driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click() # previous arrow

    dates = driver.find_elements(By.XPATH, "//tbody/tr//td//a")
    for dt in dates:
        if dt.text == date:
            dt.click()
            print(curr_month, dt.text, curr_year)
            break

time.sleep(3)