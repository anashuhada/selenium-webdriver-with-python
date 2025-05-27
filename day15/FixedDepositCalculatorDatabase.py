import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

import mysql.connector

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

try:
    con = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="root", database="mydatabase")
    curs = con.cursor()  # create cursor
    curs.execute("SELECT * FROM caldata")  # execute query through cursor
    for row in curs:
        principle = row[0]
        rate_of_interest = row[1]
        period1 = row[2]
        period2 = row[3]
        frequency = row[4]
        expected_maturity_value = row[5]

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
        else:
            print("Test failed")

        driver.find_element(By.XPATH, "//img[@class='PL5']").click()
        time.sleep(5)
    con.close()
except:
    print("Connection unsuccessful established...")

driver.close()
