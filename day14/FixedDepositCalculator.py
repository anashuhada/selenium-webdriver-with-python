import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from day14 import ExcelUtils

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file_path = "/Volumes/KINGSTON/Software Testing/calculator_data.xlsx"

rows = ExcelUtils.get_row_count(file_path, "Sheet1")
for r in range(2, rows + 1):
    principle = ExcelUtils.read_data(file_path, "Sheet1", r, 1)
    rate_of_interest = ExcelUtils.read_data(file_path, "Sheet1", r, 2)
    period1 = ExcelUtils.read_data(file_path, "Sheet1", r, 3)
    period2 = ExcelUtils.read_data(file_path, "Sheet1", r, 4)
    frequency = ExcelUtils.read_data(file_path, "Sheet1", r, 5)
    expected_maturity_value = ExcelUtils.read_data(file_path, "Sheet1", r, 6)

    # passing data to the application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rate_of_interest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period1)

    year_dropdown = driver.find_element(By.XPATH, "//select[@id='tenurePeriod']")
    period2_dropdown = Select(year_dropdown)
    period2_dropdown.select_by_visible_text(period2)

    frequency_dropdown = driver.find_element(By.XPATH, "//select[@id='frequency']")
    freq = Select(frequency_dropdown)
    freq.select_by_visible_text(frequency)

    time.sleep(3)
    element = driver.find_element(By.XPATH, "//div[@class='CTR PT15']//a[1]//img")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    actual_maturity_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']//strong").text

    # validation
    if float(expected_maturity_value) == float(actual_maturity_value):
        print("Test passed")
        ExcelUtils.write_data(file_path, "Sheet1", r, 8, "Passed")
        ExcelUtils.fill_green_color(file_path, "Sheet1", r, 8)
    else:
        print("Test failed")
        ExcelUtils.write_data(file_path, "Sheet1", r, 8, "Failed")
        ExcelUtils.fill_red_color(file_path, "Sheet1", r, 8)

    driver.find_element(By.XPATH, "//img[@class='PL5']").click()
    time.sleep(5)