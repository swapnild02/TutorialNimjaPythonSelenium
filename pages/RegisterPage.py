from selenium.webdriver.common.by import By

from pages.AccountSucessPage import AccountSucessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver=driver

    __first_name_field_XPATH="//input[@id='input-firstname']"
    __last_name_field_XPATH = "//input[@id='input-lastname']"
    __email_field_XPATH="//input[@id='input-email']"
    __telephone_field_XPATH="//input[@id='input-telephone']"
    __password_field_XPATH="//input[@id='input-password']"
    __confirm_password_field_XPATH = "//input[@id='input-confirm']"
    __select_radio_button_Yes_XPATH="//label[@class='radio-inline']//input[@value='1']"
    __select_privacy_policy_XPATH="//input[@type='checkbox' and @value='1']"
    __click_on_continue_button="//input[@type='submit' and @value='Continue']"
    __duplicate_email_warning_message_XPATH="//div[@class='alert alert-danger alert-dismissible']"
    __first_name_warning_message_XPATH= "//input[@id='input-firstname']//following-sibling::div"
    __last_name_warning_message_XPATH = "//input[@id='input-lastname']//following-sibling::div"
    __email_warning_message_XPATH="//input[@id='input-email']//following-sibling::div"
    __telephone_warning_message_XPATH="//input[@id='input-telephone']//following-sibling::div"
    __password_warning_message_XPATH="//input[@id='input-password']//following-sibling::div"

    def enter_first_name(self,first_name):
        self.send_data(first_name,"__first_name_field_XPATH",self.__first_name_field_XPATH)
        # self.driver.find_element(By.XPATH,self.__first_name_field_XPATH).click()
        # self.driver.find_element(By.XPATH,self.__first_name_field_XPATH).clear()
        # self.driver.find_element(By.XPATH,self.__first_name_field_XPATH).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.send_data(last_name, "__last_name_field_XPATH", self.__last_name_field_XPATH)
        # self.driver.find_element(By.XPATH,self.__last_name_field_XPATH).click()
        # self.driver.find_element(By.XPATH,self.__last_name_field_XPATH).clear()
        # self.driver.find_element(By.XPATH,self.__last_name_field_XPATH).send_keys(last_name)

    def enter_email(self,email_text):
        self.send_data(email_text, "__email_field_XPATH", self.__email_field_XPATH)
        # self.driver.find_element(By.XPATH,self.__email_field_XPATH).click()
        # self.driver.find_element(By.XPATH,self.__email_field_XPATH).clear()
        # self.driver.find_element(By.XPATH,self.__email_field_XPATH).send_keys(email_text)

    def enter_telephone(self,telephone_text):
        self.send_data(telephone_text, ".__telephone_field_XPATH", self.__telephone_field_XPATH)
        # self.driver.find_element(By.XPATH,self.__telephone_field_XPATH).click()
        # self.driver.find_element(By.XPATH,self.__telephone_field_XPATH).clear()
        # self.driver.find_element(By.XPATH,self.__telephone_field_XPATH).send_keys(telephone_text)

    def enter_password(self,password_text):
        self.send_data(password_text, ".__password_field_XPATH", self.__password_field_XPATH)
        # self.driver.find_element(By.XPATH,self.__password_field_XPATH).click()
        # self.driver.find_element(By.XPATH,self.__password_field_XPATH).clear()
        # self.driver.find_element(By.XPATH,self.__password_field_XPATH).send_keys(password_text)

    def enter_confirm_password(self, confirm_password_text):
        self.send_data(confirm_password_text, ".__confirm_password_field_XPATH", self.__confirm_password_field_XPATH)
        # self.driver.find_element(By.XPATH, self.__confirm_password_field_XPATH).click()
        # self.driver.find_element(By.XPATH, self.__confirm_password_field_XPATH).clear()
        # self.driver.find_element(By.XPATH, self.__confirm_password_field_XPATH).send_keys(confirm_password_text)

    def select_radio_button(self,suscribe="Unknown"):
        if suscribe=="Yes":
            self.click_on_webelement("__select_radio_button_Yes_XPATH",self.__select_radio_button_Yes_XPATH)
            # self.driver.find_element(By.XPATH, self.__select_radio_button_Yes_XPATH).click()
        else:
            pass

    def select_privacy_policy_button(self):
        self.click_on_webelement("__select_privacy_policy_XPATH",self.__select_privacy_policy_XPATH)
        # self.driver.find_element(By.XPATH, self.__select_privacy_policy_XPATH).click()

    def click_on_continue_button(self):
        self.click_on_webelement("____click_on_continue_button_XPATH", self.__click_on_continue_button)
        # self.driver.find_element(By.XPATH, self.__click_on_continue_button).click()
        return AccountSucessPage(self.driver)

    def retrived_duplicate_email_warning(self):
        return self.get_text_of_webelement("__duplicate_email_warning_message_XPATH",self.__duplicate_email_warning_message_XPATH)
        # return self.driver.find_element(By.XPATH, self.__duplicate_email_warning_message).text

    def retrived_first_name_warning(self):
        return self.get_text_of_webelement("__first_name_warning_message_XPATH",
                                           self.__first_name_warning_message_XPATH)
        # return self.driver.find_element(By.XPATH, self.__first_name_warning_message).text

    def retrived_last_name_warning(self):
        return self.get_text_of_webelement("__last_name_warning_message_XPATH",
                                           self.__last_name_warning_message_XPATH)
        # return self.driver.find_element(By.XPATH, self.__last_name_warning_message).text

    def retrived_email_warning(self):
        return self.get_text_of_webelement("__email_warning_message_XPATH",
                                           self.__email_warning_message_XPATH)
        # return self.driver.find_element(By.XPATH, self.__email_warning_message).text

    def retrived_telephone_warning(self):
        return self.get_text_of_webelement("__telephone_warning_message_XPATH",
                                           self.__telephone_warning_message_XPATH)
        # return self.driver.find_element(By.XPATH, self.__telephone_warning_message).text

    def retrived_password_warning(self):
        return self.get_text_of_webelement("__password_warning_message_XPATH",
                                           self.__password_warning_message_XPATH)
        # return self.driver.find_element(By.XPATH, self.__password_warning_message).text

