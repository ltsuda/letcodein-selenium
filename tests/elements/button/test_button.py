import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.webelement import element


class TestButton:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://demoqa.com/buttons")

        # elements
        self.double_click_button = element(self.driver, (By.CSS_SELECTOR, "#doubleClickBtn"))
        self.right_click_button = element(self.driver, (By.CSS_SELECTOR, "#rightClickBtn"))
        self.click_button = element(self.driver, (By.XPATH, "//*[text()='Click Me']"))
        self.double_click_output = element(self.driver, (By.CSS_SELECTOR, "#doubleClickMessage"))
        self.right_click_output = element(self.driver, (By.CSS_SELECTOR, "#rightClickMessage"))
        self.dynamic_click_output = element(self.driver, (By.CSS_SELECTOR, "#dynamicClickMessage"))

    def test_double_click(self):
        self.double_click_button.double_click()
        assert self.double_click_output.text() == "You have done a double click"

    def test_right_click(self):
        self.right_click_button.right_click()
        assert self.right_click_output.text() == "You have done a right click"

    def test_dynamic_click(self):
        self.click_button.click()
        assert self.dynamic_click_output.text() == "You have done a dynamic click"

    def test_one_click_on_double_click_button(self):
        self.double_click_button.click()
        assert self.double_click_output.element_is_not_present()

    def test_left_click_on_right_click_button(self):
        self.right_click_button.click()
        assert self.right_click_output.element_is_not_present()

    def test_right_click_on_dynamic_click_button(self):
        self.click_button.right_click()
        assert self.dynamic_click_output.element_is_not_present()
