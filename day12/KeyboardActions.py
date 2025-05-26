# •	Ctrl + A
# •	Ctrl + C
# •	Tab
# •	Ctrl + V

import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input_text1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input_text2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input_text1.send_keys("Welcome to Selenium")

act = ActionChains(driver)

# CTRL + A
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()

# CTRL + C
act.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()

# TAB
act.send_keys(Keys.TAB).perform()

# CTRL + V
act.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()

time.sleep(5)