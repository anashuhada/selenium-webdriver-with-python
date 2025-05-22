import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")

email_box = driver.find_element(By.XPATH, "//input[@id='email']")
email_box.clear()
email_box.send_keys("abc@gmail.com")
print("Result of text:", email_box.text) # returns inner text of the element; text for inner text >text here<
print("Result of get_attribute:", email_box.get_attribute('value'))

home_link = driver.find_element(By.XPATH, "//div[@id='PageList1']//a[normalize-space()='Home']")
print("Result of text:", home_link.text)
print("Result of get_attribute:", home_link.get_attribute('value'))
print("Result of get_attribute:", home_link.get_attribute('type'))

time.sleep(5)