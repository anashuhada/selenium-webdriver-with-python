import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

driver.find_element(By.XPATH, "//i[@class='fa fa-user']").click()
register_link = Keys.COMMAND + Keys.RETURN
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").send_keys(register_link)

# open a new tab and switch to a new tab
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.switch_to.new_window('tab')
time.sleep(3)

# switch to a new window
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.switch_to.new_window('window')
time.sleep(3)