import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# scroll down page by pixel
driver.execute_script("window.scrollBy(0, 3000)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)

time.sleep(5)

# scroll down page until the element is visible
flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Malaysia']")
driver.execute_script("arguments[0].scrollIntoView();", flag)
flag_value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", flag_value)

time.sleep(5)

# scroll down the page until end of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
doc_value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", doc_value)
time.sleep(3)

# scroll up to starting position
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
time.sleep(5)