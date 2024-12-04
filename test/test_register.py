import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.AccountSucessPage import AccountSucessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from test.BaseTest import BaseTest



class TestRegister(BaseTest):
    driver=None

    def test_register_with_mandatory_field(self):
        home_page=HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page=home_page.select_register_option()
        register_page.enter_first_name("L1")
        register_page.enter_last_name("L1")
        register_page.enter_email("s25s@gmail.com")
        register_page.enter_telephone("3546754873")
        register_page.enter_password("1234")
        register_page.enter_confirm_password("1234")
        register_page.select_radio_button()
        time.sleep(3)
        register_page.select_privacy_policy_button()
        time.sleep(3)
        account_success=register_page.click_on_continue_button()
        time.sleep(3)
        expected_text="Your Account Has Been Created!"
        assert expected_text.__eq__(account_success.retrived_account_creation_message())


    def test_register_with_all_field(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page =home_page.select_register_option()
        register_page.enter_first_name("L1")
        register_page.enter_last_name("L1")
        register_page.enter_email("s26s@gmail.com")
        register_page.enter_telephone("3546754873")
        register_page.enter_password("1234")
        register_page.enter_confirm_password("1234")
        register_page.select_radio_button()
        register_page.select_privacy_policy_button()
        account_success =register_page.click_on_continue_button()
        time.sleep(3)
        expected_text = "Your Account Has Been Created!"
        assert expected_text.__eq__(account_success.retrived_account_creation_message())

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page =home_page.select_register_option()
        register_page.enter_first_name("L1")
        register_page.enter_last_name("L1")
        register_page.enter_email("s1s@gmail.com")
        register_page.enter_telephone("3546754873")
        register_page.enter_password("1234")
        register_page.enter_confirm_password("1234")
        # Below script click on YES radio button
        register_page.select_radio_button("Yes")
        register_page.select_privacy_policy_button()
        register_page.click_on_continue_button()
        expected_text="Warning: E-Mail Address is already registered!"
        assert expected_text.__eq__(register_page.retrived_duplicate_email_warning())


    def test_without_entering_field(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page =home_page.select_register_option()
        register_page.enter_first_name("")
        register_page.enter_last_name("")
        register_page.enter_email("")
        register_page.enter_telephone("")
        register_page.enter_password("")
        register_page.enter_confirm_password("")
        register_page.click_on_continue_button()

        expected_privacy_policy_text="Warning: You must agree to the Privacy Policy!"
        assert expected_privacy_policy_text.__eq__(register_page.retrived_duplicate_email_warning())

        expected_firstname_warning="First Name must be between 1 and 32 characters!"
        assert expected_firstname_warning.__eq__(register_page.retrived_first_name_warning())

        expected_lastname_warning = "Last Name must be between 1 and 32 characters!"
        assert expected_lastname_warning.__eq__(register_page.retrived_last_name_warning())

        expected_email_warning = "E-Mail Address does not appear to be valid!"
        assert expected_email_warning.__eq__(register_page.retrived_email_warning())

        expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
        assert expected_telephone_warning.__eq__(register_page.retrived_telephone_warning())

        expected_password_warning = "Password must be between 4 and 20 characters!"
        assert expected_password_warning.__eq__(register_page.retrived_password_warning())




