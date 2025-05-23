from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opt)

driver.get("https://whatmylocation.com/")
driver.maximize_window()