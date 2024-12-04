from selenium.webdriver.common.by import By

from PageInterface.LoginPageInterface import LoginPageInterface
from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


class LoginPage(BasePage,LoginPageInterface):

    def __init__(self,driver):
        super().__init__(driver)
        # self.driver=driver

    __email_address_field_XPATH="//input[@id='input-email']"
    __password_field_XPATH="//input[@id='input-password']"
    __login_button_XPATH="//input[@type='submit']"
    __warning_message_XPATH="//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self,email_address):
        self.send_data(email_address,"__email_address_field_XPATH",self.__email_address_field_XPATH)
        # self.driver.find_element(By.XPATH,self.__email_address_field_XPATH).click()
        # self.driver.find_element(By.XPATH, self.__email_address_field_XPATH).clear()
        # self.driver.find_element(By.XPATH, self.__email_address_field_XPATH).send_keys(email_address)
    def enter_password(self,password_text):
        self.send_data(password_text, "__password_field_XPATH", self.__password_field_XPATH)
        # self.driver.find_element(By.XPATH,self.__password_field_XPATH).click()
        # self.driver.find_element(By.XPATH, self.__password_field_XPATH).clear()
        # self.driver.find_element(By.XPATH, self.__password_field_XPATH).send_keys(password_text)

    def click_on_login_button(self):
        self.click_on_webelement("__login_button_XPATH",self.__login_button_XPATH)
        # self.driver.find_element(By.XPATH, self.__login_button_XPATH).click()
        return AccountPage(self.driver)

    def retrieve_warning_message(self):
        actual_text=self.get_text_of_webelement("__warning_message_XPATH",self.__warning_message_XPATH)
        return actual_text
        # return self.driver.find_element(By.XPATH, self.__warning_message_XPATH).text