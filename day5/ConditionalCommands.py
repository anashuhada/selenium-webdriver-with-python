import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# is_displayed & is_enabled
search_box = driver.find_element(By.XPATH, "//input[@id='name']")
print("Display status:", search_box.is_displayed()) # True
print("Enable status:", search_box.is_enabled()) # True

# is_selected - radio buttons and checkboxes
radio_button_male = driver.find_element(By.XPATH, "//input[@id='male']")
radio_button_female = driver.find_element(By.XPATH, "//input[@id='female']")

print("Before selecting male radio button...")
print("Male radio button is selected:", radio_button_male.is_selected()) # False
print("Female radio button is selected:", radio_button_female.is_selected()) # False

print("After selecting male radio button...")
radio_button_male.click()

print("Male radio button is selected:", radio_button_male.is_selected()) # True
print("Female radio button is selected:", radio_button_female.is_selected()) # False

time.sleep(5)
# driver.close()
driver.quit()