import pytest
from pages.HomePage import HomePage
from test.BaseTest import BaseTest
from utilities.custom_logger import Log_Maker


class TestSearch(BaseTest):
    driver = None

    @pytest.mark.e2e
    def test_search_for_valid_product(self):
        self.logger.info("TestSearch started")
        self.logger.info(20*"*")
        home_page=HomePage(self.driver)
        self.logger.info("Enter product Name HP")
        home_page.enter_product_into_search_box_field("HP")
        self.logger.info("click on button")
        search_page=home_page.click_on_search_button()
        self.logger.info("Product name displayed")
        assert search_page.display_status_of_product()
    @pytest.mark.smoke
    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("Honda")
        search_page=home_page.click_on_search_button()
        expected_test="There is no product that matches the search criteria."
        actual_text=search_page.retrived_no_product_message()
        print("Actual text is :- ",actual_text)
        assert  expected_test.__eq__(actual_text)

    @pytest.mark.initinal
    def test_search_without_any_entering_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("")
        search_page=home_page.click_on_search_button()
        expected_test = "There is no product that matches the search criteria."
        assert expected_test.__eq__(search_page.retrived_no_product_message())