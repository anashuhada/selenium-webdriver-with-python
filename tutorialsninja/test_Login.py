import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("alex.smith@yopmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("P@ssw0rd#123")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        message = self.driver.find_element(By.XPATH, "//h2[normalize-space()='My Account']")
        assert message.is_displayed()

    def test_login_without_providing_credentials(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        actual_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
        assert actual_message.__contains__(expected_message)
