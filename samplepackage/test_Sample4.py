import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_tutorial_ninja():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()

    expected_title = "Your Store"
    actual_title = driver.title

    # hard assertion
    assert actual_title.__eq__(expected_title)

    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("HP")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.XPATH, "//a[normalize-space()='HP LP3065']").is_displayed()

    time.sleep(3)
    driver.quit()

    # soft assertion - use flag: --soft-asserts