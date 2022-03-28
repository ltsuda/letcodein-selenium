import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.webelement import element


class TestTextBox:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://demoqa.com/text-box")

        # elements
        self.full_name_input = element(self.driver, (By.CSS_SELECTOR, "#userName"))
        self.email_input = element(self.driver, (By.CSS_SELECTOR, "#userEmail"))
        self.current_address_textarea = element(self.driver, (By.CSS_SELECTOR, "#currentAddress"))
        self.permanent_address_textarea = element(
            self.driver, (By.CSS_SELECTOR, "#permanentAddress")
        )
        self.submit_button = element(self.driver, (By.CSS_SELECTOR, "#submit"))
        self.output_name = element(self.driver, (By.CSS_SELECTOR, "#output #name"))
        self.output_email = element(self.driver, (By.CSS_SELECTOR, "#output #email"))
        self.output_current_address = element(
            self.driver, (By.CSS_SELECTOR, "#output #currentAddress")
        )
        self.output_permanent_address = element(
            self.driver, (By.CSS_SELECTOR, "#output #permanentAddress")
        )

        # variables
        self.name = "John Doe"
        self.email = "j.doe@provider.com"
        self.current_address = "1 Infinite Loop, Cupertino, CA 95014, US"
        self.permanent_address = "1 Apple Park Way, Cupertino, CA 95014"

    def test_text_box(self):
        self.full_name_input.send_keys(self.name)
        self.email_input.send_keys(self.email)
        self.current_address_textarea.send_keys(self.current_address)
        self.permanent_address_textarea.send_keys(self.permanent_address)
        self.submit_button.click()

        assert self.output_name.contain_text(self.name)
        assert self.output_email.contain_text(self.email)
        assert self.output_current_address.contain_text(self.current_address)
        assert self.output_permanent_address.contain_text(self.permanent_address)

    def test_text_box_invalid_email(self):
        self.full_name_input.send_keys(self.name)
        self.email_input.send_keys("invalid@email")
        self.current_address_textarea.send_keys(self.current_address)
        self.permanent_address_textarea.send_keys(self.permanent_address)
        self.submit_button.click()

        assert self.output_email.element_is_not_present()
        assert self.email_input.contain_class("field-error")
