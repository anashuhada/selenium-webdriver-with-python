import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# single frame
# driver.switch_to.frame("SingleFrame") # frame name
# iframe_text = driver.find_element(By.XPATH, "//div[@class='container']//h5")
# print(iframe_text.text)
# time.sleep(5)

# multiple frame
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
outer_frame  = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)
outer_text = driver.find_element(By.XPATH, "//div[@class='iframe-container']//h5")
print(outer_text.text)

# driver.switch_to.default_content()

inner_frame = driver.find_element(By.XPATH, "//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
driver.switch_to.frame(inner_frame)
inner_text = driver.find_element(By.XPATH, "//h5[normalize-space()='iFrame Demo']")
print(inner_text.text)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Selenium")

driver.switch_to.parent_frame() # directly switch to parent frame/outer frame

time.sleep(5)