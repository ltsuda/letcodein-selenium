from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.consts import URL
from src.pages.base_page import BasePage
from src.webelement import Locator, base_element


class TextboxSelectors:
    full_name_input: str = "#userName"
    email_input: str = "#userEmail"
    current_address_textarea: str = "#currentAddress"
    permanent_address_textarea: str = "#permanentAddress"
    submit_button: str = "#submit"
    output_name: str = "#output #name"
    output_email: str = "#output #email"
    output_current_address: str = "#output #currentAddress"
    output_permanent_address: str = "#output #permanentAddress"


class TextboxLocator:
    full_name_input: Locator = (By.CSS_SELECTOR, TextboxSelectors.full_name_input)
    email_input: Locator = (By.CSS_SELECTOR, TextboxSelectors.email_input)
    current_address_textarea: Locator = (
        By.CSS_SELECTOR,
        TextboxSelectors.current_address_textarea,
    )
    permanent_address_textarea: Locator = (
        By.CSS_SELECTOR,
        TextboxSelectors.permanent_address_textarea,
    )
    submit_button: Locator = (By.CSS_SELECTOR, TextboxSelectors.submit_button)
    output_name: Locator = (By.CSS_SELECTOR, TextboxSelectors.output_name)
    output_email: Locator = (By.CSS_SELECTOR, TextboxSelectors.output_email)
    output_current_address: Locator = (By.CSS_SELECTOR, TextboxSelectors.output_current_address)
    output_permanent_address: Locator = (
        By.CSS_SELECTOR,
        TextboxSelectors.output_permanent_address,
    )


class TextboxPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def goto(self):
        super().goto(URL.TEXTBOX)

    def full_name_input(self):
        return base_element(self.driver, TextboxLocator.full_name_input)

    def email_input(self):
        return base_element(self.driver, TextboxLocator.email_input)

    def current_address_textarea(self):
        return base_element(self.driver, TextboxLocator.current_address_textarea)

    def permanent_address_textarea(self):
        return base_element(self.driver, TextboxLocator.permanent_address_textarea)

    def submit_button(self):
        return base_element(self.driver, TextboxLocator.submit_button)

    def output_name(self):
        return base_element(self.driver, TextboxLocator.output_name)

    def output_email(self):
        return base_element(self.driver, TextboxLocator.output_email)

    def output_current_address(self):
        return base_element(self.driver, TextboxLocator.output_current_address)

    def output_permanent_address(self):
        return base_element(self.driver, TextboxLocator.output_permanent_address)
