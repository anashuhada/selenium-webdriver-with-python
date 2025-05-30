import time

import allure
import pytest
from allure_commons.types import AttachmentType

from selenium import webdriver


# @pytest.fixture(params=["chrome", "firefox", "edge"]) - parameterization
@pytest.fixture()
def setup_and_teardown(request):
    global driver
    # if request.param == "chrome": # parameterization
    #     driver = webdriver.Chrome()
    # elif request.param == "firefox":
    #     driver = webdriver.Firefox()
    # else:
    #     driver = webdriver.Edge()

    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("Browser not supported")

    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    request.cls.driver = driver  # attaches driver to the test class
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="failure_screenshot",
                      attachment_type=AttachmentType.PNG)
    time.sleep(3)
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# @pytest.fixture(autouse=True)
# def capture_failure_screenshot(request):
#     yield
#     if request.node.rep_call.failed:
#         driver = getattr(request.cls, "driver", None)
#         if driver:
#             allure.attach(driver.get_screenshot_as_png(),
#                           name="failure_screenshot",
#                           attachment_type=AttachmentType.PNG)


def pytest_addoption(parser):
    parser.addoption("--browser")
    # parser.addoption("--platform")
