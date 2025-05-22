import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# driver.implicitly_wait(10) # implicit wait

# explicit wait
# wait = WebDriverWait(driver, 10) # basic
wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])

search_box = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
search_box.send_keys("Selenium")
search_box.submit()

# time.sleep(3)
search_element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Selenium']")))
search_element.click()

time.sleep(5)