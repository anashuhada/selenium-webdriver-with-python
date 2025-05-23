from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# count number of rows and columns
num_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
num_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]//th"))

# print(num_rows) # 7
# print(num_columns) # 4

# read specific row & column data
data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]//td[1]").text
print(data) # Master In Selenium

# read all the rows
for r in range(2, num_rows + 1):
    for c in range(1, num_columns):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]//td[" + str(c) + "]").text
        print(data, end=' | ')
    print()

# read data based on condition list books name whose author is Mukesh
for r in range(2, num_rows + 1):
    author = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]//td[2]").text
    if author == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]//td[1]").text
        book_price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]//td[4]").text
        print("Author: ", author, "| Book Name:", book_name, "| Price:", book_price)