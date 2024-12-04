import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from test.BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):
    driver=None

    @pytest.mark.parametrize("email_address,password",ExcelUtils.get_data_from_excel())
    def test_login_with_valid_credential(self,email_address,password):
        home_page=HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page=home_page.select_login_option()
        login_page.enter_email_address(email_address)
        login_page.enter_password(password)
        account_page=login_page.click_on_login_button()
        account_page.display_status_of_edit_your_account_information_option()

    def test_login_with_invalidemail_and_validpassword_crenditial(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page =home_page.select_login_option()
        login_page.enter_email_address("swapnild0211@gmail.com")
        login_page.enter_password("1234")
        login_page.click_on_login_button()
        expected_text="Warning: No match for E-Mail Address and/or Password."
        assert expected_text.__eq__(login_page.retrieve_warning_message())

    def test_login_with_validemail_and_invalidpassword_crenditial(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page =home_page.select_login_option()
        login_page.enter_email_address("swapnild02@gmail.com")
        login_page.enter_password("12ygt")
        login_page.click_on_login_button()
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert expected_text.__eq__(login_page.retrieve_warning_message())


    def test_login_without_entering_crenditial(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page =home_page.select_login_option()
        login_page.enter_email_address("")
        login_page.enter_password("")
        login_page.click_on_login_button()
        expected_text="Warning: No match for E-Mail Address and/or Password."
        assert expected_text.__eq__(login_page.retrieve_warning_message())