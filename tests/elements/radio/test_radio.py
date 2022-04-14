import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.consts import URL
from src.pages.elements.radio.radio_page import RadioPage


class TestRadio:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.radio_button_page = RadioPage(driver)
        self.radio_button_page.goto()
        self.radio_button_page.wait_until_url(URL.RADIO)

    def test_select_yes(self):
        self.radio_button_page.yes_radio_button().click()
        assert self.radio_button_page.output().contain_text("You have selected Yes")

    def test_select_impressive(self):
        self.radio_button_page.impressive_radio_button().click()
        assert self.radio_button_page.output().contain_text("You have selected Impressive")

    def test_no_radio_button_is_disabled(self):
        assert self.radio_button_page.no_radio_button().is_enabled() is False
