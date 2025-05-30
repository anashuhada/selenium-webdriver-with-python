import time
import random
import pytest
from selenium.webdriver.common.by import By


def random_string():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    length = 10
    result = []

    for _ in range(length):
        result.append(random.choice(chars))

    return ''.join(result)


def random_numeric():
    digits = "0123456789"
    length = 10
    result = []

    for _ in range(length):
        result.append(random.choice(digits))

    return ''.join(result)


def random_alphanumeric():
    return random_string() + random_numeric()


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_create_account_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys(random_string())
        self.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys(random_string())
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(random_string() + "@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys(random_numeric())
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_message = "Your Account Has Been Created!"
        time.sleep(2)
        actual_message = self.driver.find_element(By.XPATH,
                                                  "//h1[normalize-space()='Your Account Has Been Created!']").text
        assert expected_message in actual_message

    def test_create_account_by_providing_all_fields(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys(random_string())
        self.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys(random_string())
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(random_string() + "@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys(random_numeric())
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys("12345")
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']//input[@name='newsletter']").click()
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_message = "Your Account Has Been Created!'"
        actual_message = self.driver.find_element(By.XPATH,
                                                  "//h1[normalize-space()='Your Account Has Been Created!']").text
        assert expected_message in actual_message
