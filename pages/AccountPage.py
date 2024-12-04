from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        # self.driver=driver

    __edit_your_account_information_option_XPATH="//ul[@class='list-unstyled']//li//a[text()='Edit your account information']"

    def display_status_of_edit_your_account_information_option(self):
       return self.is_displaying("__edit_your_account_information_option_XPATH",self.__edit_your_account_information_option_XPATH)
       # return self.driver.find_element(By.XPATH,self.__edit_your_account_information_option_link_text).is_displayed()