import string

from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def locators(self,locatorname,locator):
        element = None
        if locatorname.__contains__("_ID"):
            element = self.driver.find_element(By.ID, locator)
        elif locatorname.__contains__("_NAME"):
            element = self.driver.find_element(By.NAME, locator)
        elif locatorname.__contains__("_LINK_TEXT"):
            element = self.driver.find_element(By.LINK_TEXT, locator)
        elif locatorname.__contains__("_TAG_NAME"):
            element = self.driver.find_element(By.TAG_NAME, locator)
        elif locatorname.__contains__("_CLASS_NAME"):
            element = self.driver.find_element(By.CLASS_NAME, locator)
        elif locatorname.__contains__("_XPATH"):
            element = self.driver.find_element(By.XPATH, locator)
        elif locatorname.__contains__("_CSS_SELECTOR"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
        else:
            raise "Please provide correct locator"
        return element

    def send_data(self,text,locatorname,locator):
        element=self.locators(locatorname,locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_on_webelement(self, locatorname: object, locator: object) -> object:
        """
This method is use to click on web element
        :param text:
        :param locatorname:
        :param locator:
        """
        element = self.locators(locatorname,locator)
        element.click()

    def is_displaying(self,locatorname,locator):
        element = self.locators(locatorname, locator)
        return element.is_displayed()

    def get_text_of_webelement(self,locatorname,locator):
        element = self.locators(locatorname, locator)
        return element.text






