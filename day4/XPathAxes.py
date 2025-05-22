import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# self
self_msg = driver.find_element(By.XPATH, "//a[contains(text(), '3M India')]/self::a")
print(self_msg.text)

# parent
parent_msg = driver.find_element(By.XPATH, "//a[contains(text(), '3M India')]/parent::td")
print(parent_msg.text)

# child
child_msg = driver.find_elements(By.XPATH, "//a[contains(text(), '3M India')]/ancestor::tr/child::td")
print(len(child_msg))

for child in child_msg:
    print(child.text)

# ancestor
ancestor_msg = driver.find_element(By.XPATH, "//a[contains(text(), '3M India')]/ancestor::tr")
print(ancestor_msg.text)

# descendant
descendant_msg = driver.find_elements(By.XPATH, "//a[contains(text(), '3M India')]/ancestor::tr/descendant::*")
print(len(descendant_msg))

for desc in descendant_msg:
    print(desc.text)

# following
following_msg = driver.find_elements(By.XPATH, "//a[contains(text(), '3M India')]/ancestor::tr/following::*")
print(len(following_msg))

for fol in following_msg:
    print(fol.text)

# following sibling
following_sib = driver.find_elements(By.XPATH, "//a[contains(text(), '3M India')]/ancestor::tr/following-sibling::*")
print(len(following_sib))

for fol_sib in following_sib:
    print(fol_sib.text)

# preceding
preceding = driver.find_elements(By.XPATH, "//a[contains(text(), '3M India')]/ancestor::tr/preceding::tr")
print(len(preceding))

for prec in preceding:
    print(prec.text)

# preceding sibling
preceding_sib = driver.find_elements(By.XPATH, "//a[contains(text(), '3M India')]/ancestor::tr/preceding::*")
print(len(preceding_sib))

for prec_sib in preceding_sib:
    print(prec_sib.text)

time.sleep(5)