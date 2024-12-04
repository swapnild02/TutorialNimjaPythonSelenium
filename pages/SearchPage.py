from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        # self.driver=driver

    __valid_hp_product_LINK_TEXT="HP LP3065"

    # def display_status_of_product(self):
    #   return self.driver.find_element(By.LINK_TEXT,self.__valid_hp_product_LINK_TEXT).is_displayed()

    def display_status_of_product(self):
        return self.is_displaying("__valid_hp_product_LINK_TEXT",self.__valid_hp_product_LINK_TEXT)
      # return self.driver.find_element(By.LINK_TEXT,self.__valid_hp_product_LINK_TEXT).is_displayed()

    no_product_message_XPATH="//input[@id='button-search']/following-sibling::p"

    # def retrived_no_product_message(self):
    #    return self.driver.find_element(By.XPATH,self.no_product_message_XPATH).text

    def retrived_no_product_message(self):
        actual_text= self.get_text_of_webelement("no_product_message_XPATH",self.no_product_message_XPATH)
        return actual_text


