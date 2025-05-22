import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# absolute xpath
driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("Camelia")

# relative xpath
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Camelia")

# use or operator
driver.find_element(By.XPATH, "//input[@placeholder='Enter Name' or @id='name']").send_keys("Camelia")

# use and operator
driver.find_element(By.XPATH, "//input[@placeholder='Enter Name' and @id='name']").send_keys("Camelia")

# use contains()
driver.find_element(By.XPATH, "//input[contains(@id, 'name')]").send_keys("Camelia")

# use starts-with()
driver.find_element(By.XPATH,"//input[starts-with(@placeholder, 'Enter EM')]").send_keys("camelia@example.com")

# use text() - inner text
driver.find_element(By.XPATH,"//label[text()='Name:']")

time.sleep(5)