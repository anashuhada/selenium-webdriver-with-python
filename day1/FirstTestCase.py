import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# open web browser
# open url https://opensource-demo.orangehrmlive.com/
# enter username: Admin
# enter password: admin123
# click on login button
# capture title of the home page - actual title
# verify title of the home page: OrangeHRM - expected
# close browser

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
username = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username.send_keys("Admin")

password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("admin123")

login = driver.find_element(By.XPATH, "//button[@type='submit']")
login.click()

actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("Login test passed")
else:
    print("Login test failed")

time.sleep(5)

driver.quit()
