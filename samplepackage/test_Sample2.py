import time

from selenium import webdriver


def test_omayo():
    driver = webdriver.Chrome()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()


def test_tutorial_ninja():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()


def test_selenium_143():
    driver = webdriver.Chrome()
    driver.get("https://selenium143.blogspot.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()


def test_selenium_by_arun():
    driver = webdriver.Chrome()
    driver.get("https://selenium-by-arun.blogspot.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()


def test_herokuapp():
    driver = webdriver.Chrome()
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()


def test_jquery():
    driver = webdriver.Chrome()
    driver.get("https://jquery.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()
