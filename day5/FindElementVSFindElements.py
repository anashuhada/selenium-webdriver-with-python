import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")

# find_element - returns single web element
# locator matching with single web element
element = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
element.send_keys("Selenium")

# locator matching with multiple web elements
footer = driver.find_element(By.XPATH, "//div[@class='widget PageList' and @id='PageList1']//a") # returns the first web element
print(footer.text) # Home

# element not available then throw NoSuchElementException
name_element = driver.find_element(By.ID, "nam")
name_element.click()

# find_elements - returns multiple web elements
# locator matching with single web element
elements = driver.find_elements(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
print(len(elements)) # 1
print(elements[0].send_keys("Selenium"))

# locator matching with multiple web elements
footer_elements = driver.find_elements(By.XPATH, "//div[@class='widget PageList' and @id='PageList1']//a")
print(len(footer_elements)) # 3
print(footer_elements[0].text) # Home
for foot in footer_elements:
    print(foot.text)

# element not available - returns 0
name_elements = driver.find_elements(By.ID, "nam")
print("Elements returned:", len(name_elements)) # Elements returned: 0

time.sleep(5)