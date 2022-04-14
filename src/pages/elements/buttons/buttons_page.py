from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.consts import URL
from src.pages.base_page import BasePage
from src.webelement import Locator, base_element


class ButtonSelectors:
    double_click = "#doubleClickBtn"
    right_click = "#rightClickBtn"
    click = "//*[text()='Click Me']"
    double_click_output = "#doubleClickMessage"
    right_click_output = "#rightClickMessage"
    dynamic_click_output = "#dynamicClickMessage"


class ButtonLocator:
    double_click: Locator = (By.CSS_SELECTOR, ButtonSelectors.double_click)
    right_click_button: Locator = (By.CSS_SELECTOR, ButtonSelectors.right_click)
    click_button: Locator = (By.XPATH, ButtonSelectors.click)
    double_click_output: Locator = (By.CSS_SELECTOR, ButtonSelectors.double_click_output)
    right_click_output: Locator = (By.CSS_SELECTOR, ButtonSelectors.right_click_output)
    dynamic_click_output: Locator = (By.CSS_SELECTOR, ButtonSelectors.dynamic_click_output)


class ButtonsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def goto(self):
        super().goto(URL.BUTTONS)

    def double_click_button(self):
        return base_element(self.driver, ButtonLocator.double_click)

    def right_click_button(self):
        return base_element(self.driver, ButtonLocator.right_click_button)

    def click_button(self):
        return base_element(self.driver, ButtonLocator.click_button)

    def double_click_output(self):
        return base_element(self.driver, ButtonLocator.double_click_output)

    def right_click_output(self):
        return base_element(self.driver, ButtonLocator.right_click_output)

    def dynamic_click_output(self):
        return base_element(self.driver, ButtonLocator.dynamic_click_output)
