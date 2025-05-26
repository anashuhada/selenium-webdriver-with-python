import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(button).perform()

time.sleep(3)

driver.find_element(By.XPATH, "//span[normalize-space()='Paste']").click()
driver.switch_to.alert.accept()

time.sleep(5)