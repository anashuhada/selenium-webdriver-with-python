from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

cookies = driver.get_cookies() # capture cookies from the browser
print("Size of cookies:", len(cookies)) # 3

# print details of all cookies
for c in cookies:
    #print(c)
    print(c.get("name"), ":" , c.get("value"))

# add new cookie to the browser
driver.add_cookie({"name": "MyCookie", "value": "12345"})
cookies = driver.get_cookies()
print("New size of cookies:", len(cookies)) # 4

# remove specific cookie from the browser
driver.delete_cookie("MyCookie")
print("Size of cookies after deleted one:", len(cookies))
driver.quit()

# remove all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of cookies after removing all the cookies:", len(cookies)) # 0