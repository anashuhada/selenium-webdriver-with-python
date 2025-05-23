import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

time.sleep(3)

# curr_window_id = driver.current_window_handle
# print(curr_window_id) # EDBC6100F1BC23959143389CE47E044A

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(3)

window_ids = driver.window_handles
# approach 1
# parent = window_ids[0]
# child = window_ids[1]
#
# driver.switch_to.window(child) # switch to child window
# print("Child window:", driver.title)
#
# driver.switch_to.window(parent) # switch to parent window
# print("Parent window:", driver.title)

# print(parent)
# print(child)

# approach 2
# for win_id in window_ids:
#     driver.switch_to.window(win_id)
#     print("Window ID:", driver.title)

# close specific browser window
for win_id in window_ids:
    driver.switch_to.window(win_id)
    if driver.title == "OrangeHRM":
        driver.close()

time.sleep(3)