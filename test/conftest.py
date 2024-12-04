import allure
import pytest
from allure_commons.model2 import Attachment
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions


from utilities import ReadConfiguration

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),name="Failed Screenshot",attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    headless_browser = ReadConfiguration.read_configuration("basic info", "br")
    browser=ReadConfiguration.read_configuration("basic info","browser")
    if browser.__eq__("Chrome"):
        if not headless_browser.__eq__("headless"):
            driver = webdriver.Chrome()
        else:
          driver =  chrome_option_browser(headless_browser)
    elif browser.__eq__("Edge"):
        driver= webdriver.Edge()
    elif browser.__eq__("Firefox"):
        driver = webdriver.Firefox()
    else:
        raise "Check your broswer Name"
    driver.maximize_window()
    url = ReadConfiguration.read_configuration("basic info", "url")

    driver.get(url)
    request.cls.driver=driver
    yield
    driver.quit()

def chrome_option_browser(hl=None):
    print("I am in chrome_option_browser :- ",hl)
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument(hl)
    driver = webdriver.Chrome(options=chrome_option)
    return driver










































# @pytest.fixture()
# def setup_and_teardown(request):
#     driver=None
#     headless_browser = ReadConfiguration.read_configuration("basic info", "br")
#     print("Fetching from configs.ini files :- ",headless_browser)
#     browser=ReadConfiguration.read_configuration("basic info","browser")
#     if browser.__eq__("Chrome"):
#         if not headless_browser.__eq__("headless"):
#             driver = webdriver.Chrome()
#         else:
#           driver =  chrome_option_browser(headless_browser)
#     elif browser.__eq__("Edge"):
#         driver= webdriver.Edge()
#     elif browser.__eq__("Firefox"):
#         driver = webdriver.Firefox()
#     else:
#         raise "Check your broswer Name"
#     driver.maximize_window()
#     url = ReadConfiguration.read_configuration("basic info", "url")
#
#     driver.get(url)
#     request.cls.driver=driver
#     yield
#     driver.quit()
#
# def chrome_option_browser(hl=None):
#     print("I am in chrome_option_browser :- ",hl)
#     chrome_option = webdriver.ChromeOptions()
#     chrome_option.add_argument(hl)
#     driver = webdriver.Chrome(options=chrome_option)
#     return driver
