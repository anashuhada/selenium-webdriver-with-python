import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']//span[1]")
max_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']//span[2]")

print("Location of slider before moving...")
print("Min slider:", min_slider.location, "| Max Slider:", max_slider.location) # Min slider: {'x': 59, 'y': 257} | Max Slider: {'x': 767, 'y': 257}

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -67, 0).perform()

print("Location of slider after moving...")
print("Min slider:", min_slider.location, "| Max Slider:", max_slider.location) # Min slider: {'x': 158, 'y': 257} | Max Slider: {'x': 696, 'y': 257}

time.sleep(5)