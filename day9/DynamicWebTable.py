import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

time.sleep(3)

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

time.sleep(3)

driver.find_element(By.XPATH, "//a[normalize-space()='Admin']").click()

time.sleep(3)

total_rows = len(driver.find_elements(By.XPATH, "//div[@role='table']//div[@role='rowgroup']//div[@class='oxd-table-card']//div[@role='row']"))
print(total_rows)

count = 0
for i in range(1, total_rows + 1):
    status = driver.find_element(By.XPATH, "//div[@role='rowgroup']//div[" + str(i) + "]//div[1]//div[5]//div[1]").text
    # print(status)
    if status == "Enabled":
        count += 1

print("Total number of users", total_rows)
print("Total number of enabled users", count)
print("Total number of disabled users", total_rows - count)
time.sleep(10)