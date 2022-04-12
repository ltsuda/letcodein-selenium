import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.webelement import base_element


class TestRadio:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://demoqa.com/radio-button")

        # elements
        self.yes_radio_button = base_element(
            self.driver, (By.CSS_SELECTOR, "label[for='yesRadio']")
        )
        self.impressive_radio_button = base_element(
            self.driver, (By.CSS_SELECTOR, "label[for='impressiveRadio']")
        )
        self.no_radio_button = base_element(self.driver, (By.CSS_SELECTOR, "#noRadio"))
        self.output = base_element(self.driver, (By.CSS_SELECTOR, ".mt-3"))

    def test_select_yes(self):
        self.yes_radio_button.click()
        assert self.output.contain_text("You have selected Yes")

    def test_select_impressive(self):
        self.impressive_radio_button.click()
        assert self.output.contain_text("You have selected Impressive")

    def test_no_radio_button_is_disabled(self):
        assert self.no_radio_button.is_enabled() is False
