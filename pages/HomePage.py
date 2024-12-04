from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        # self.driver=driver

    __search_box_field_NAME="search"
    __click_on_search_button_XPATH="//button[@class='btn btn-default btn-lg']"
    __my_account_drop_menu_XPATH="//span[text()='My Account']"
    __login_option_XPATH="//ul[@class='dropdown-menu dropdown-menu-right']//li//a[text()='Login']"
    __register_option_XPATH="//ul[@class='dropdown-menu dropdown-menu-right']//li//a[text()='Register']"

    # def enter_product_into_search_box_field(self,product_name):
    #     self.driver.find_element(By.NAME, self.__search_box_field_NAME).click()
    #     self.driver.find_element(By.NAME, self.__search_box_field_NAME).clear()
    #     self.driver.find_element(By.NAME,self.__search_box_field_NAME).send_keys(product_name)

    def enter_product_into_search_box_field(self,product_name):
        self.send_data(product_name,"search_box_field_NAME",self.__search_box_field_NAME)

    # def click_on_search_button(self):
    #     self.driver.find_element(By.XPATH, self.__click_on_search_button_XPATH).click()
    #     return SearchPage(self.driver)
    def click_on_search_button(self):
        self.click_on_webelement("__click_on_search_button_XPATH",self.__click_on_search_button_XPATH)
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.click_on_webelement("__my_account_drop_menu_XPATH",self.__my_account_drop_menu_XPATH)
        # self.driver.find_element(By.XPATH,self.__my_account_drop_menu_XPATH).click()

    def select_login_option(self):
        self.click_on_webelement("__login_option_XPATH",self.__login_option_XPATH)
        # self.driver.find_element(By.XPATH,self.__login_option_XPATH).click()
        return LoginPage(self.driver)

    def select_register_option(self):
        self.click_on_webelement("__register_option_XPATH", self.__register_option_XPATH)
        # self.driver.find_element(By.XPATH, self.__register_option_XPATH).click()
        return RegisterPage(self.driver)





