import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

source_element = driver.find_element(By.XPATH, "//div[@id='draggable']")
target_element = driver.find_element(By.XPATH, "//div[@id='droppable']")

act = ActionChains(driver)
act.drag_and_drop(source_element, target_element).perform()

time.sleep(5)