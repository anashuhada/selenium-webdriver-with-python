from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    service = Service(ChromeDriverManager().install())
    chrome_option = webdriver.ChromeOptions()
    chrome_option.headless = True
    driver = webdriver.Chrome(service=service, options=chrome_option)
    return driver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    service = Service(EdgeChromiumDriverManager().install())
    edge_option = webdriver.EdgeOptions()
    edge_option.headless = True
    driver = webdriver.Chrome(service=service, options=edge_option)
    return driver

def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager

    service = Service(GeckoDriverManager().install())
    firefox_option = webdriver.FirefoxOptions()
    firefox_option.headless = True
    driver = webdriver.Chrome(service=service, options=firefox_option)
    return driver

driver = headless_chrome()
driver.implicitly_wait(10)

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.close()