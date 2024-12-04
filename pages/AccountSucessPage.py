from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountSucessPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.driver=driver

    __account_creation_message_XPATH="//div[@id='content']//h1"

    def retrived_account_creation_message(self):
       return self.get_text_of_webelement("__account_creation_message_XPATH",self.__account_creation_message_XPATH)
        # return self.driver.find_element(By.XPATH,self.__account_creation_message_XPATH).text
