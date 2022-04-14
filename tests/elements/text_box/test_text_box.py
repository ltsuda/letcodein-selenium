import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.consts import URL
from src.pages.elements.text_box.text_box_page import TextboxPage


class TestTextBox:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.textbox_page = TextboxPage(driver)
        self.textbox_page.goto()
        self.textbox_page.wait_until_url(URL.TEXTBOX)

        # variables
        self.name = "John Doe"
        self.email = "j.doe@provider.com"
        self.current_address = "1 Infinite Loop, Cupertino, CA 95014, US"
        self.permanent_address = "1 Apple Park Way, Cupertino, CA 95014"

    def test_text_box(self):
        self.textbox_page.full_name_input().send_keys(self.name)
        self.textbox_page.email_input().send_keys(self.email)
        self.textbox_page.current_address_textarea().send_keys(self.current_address)
        self.textbox_page.permanent_address_textarea().send_keys(self.permanent_address)
        self.textbox_page.submit_button().click()

        assert self.textbox_page.output_name().contain_text(self.name)
        assert self.textbox_page.output_email().contain_text(self.email)
        assert self.textbox_page.output_current_address().contain_text(self.current_address)
        assert self.textbox_page.output_permanent_address().contain_text(self.permanent_address)

    def test_text_box_invalid_email(self):
        self.textbox_page.full_name_input().send_keys(self.name)
        self.textbox_page.email_input().send_keys("invalid@email")
        self.textbox_page.current_address_textarea().send_keys(self.current_address)
        self.textbox_page.permanent_address_textarea().send_keys(self.permanent_address)
        self.textbox_page.submit_button().click()

        assert self.textbox_page.output_email().element_is_not_present()
        assert self.textbox_page.email_input().contain_class("field-error")
