import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# parent window
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(3)

# child window
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()

time.sleep(5)

# this close the parent window
driver.close()