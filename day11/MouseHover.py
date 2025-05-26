import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

components = driver.find_element(By.XPATH, "//a[normalize-space()='Components']")
monitors = driver.find_element(By.XPATH, "//a[normalize-space()='Monitors (2)']")

# mouse hover
act = ActionChains(driver)
act.move_to_element(components).move_to_element(monitors).click().perform()

time.sleep(5)