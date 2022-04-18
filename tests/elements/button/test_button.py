import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.consts import URL
from src.pages.elements.buttons.buttons_page import ButtonsPage


class TestButton:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.buttons_page = ButtonsPage(driver)
        self.buttons_page.goto()
        self.buttons_page.wait_until_url(URL.BUTTONS)

    def test_double_click(self):
        self.buttons_page.double_click_button().double_click()
        assert self.buttons_page.double_click_output().text() == "You have done a double click"

    def test_right_click(self):
        self.buttons_page.right_click_button().right_click()
        assert self.buttons_page.right_click_output().text() == "You have done a right click"

    def test_dynamic_click(self):
        self.buttons_page.click_button().click()
        assert self.buttons_page.dynamic_click_output().text() == "You have done a dynamic click"

    def test_one_click_on_double_click_button(self):
        self.buttons_page.double_click_button().click()
        assert self.buttons_page.double_click_output().element_is_not_visible()

    def test_left_click_on_right_click_button(self):
        self.buttons_page.right_click_button().click()
        assert self.buttons_page.right_click_output().element_is_not_visible()

    def test_right_click_on_dynamic_click_button(self):
        self.buttons_page.click_button().right_click()
        assert self.buttons_page.dynamic_click_output().element_is_not_visible()
