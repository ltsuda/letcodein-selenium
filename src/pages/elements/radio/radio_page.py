from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.consts import URL
from src.pages.base_page import BasePage
from src.webelement import Locator, base_element


class RadioSelectors:
    yes_radio: str = "label[for='yesRadio']"
    impressive_radio: str = "label[for='impressiveRadio']"
    no_radio: str = "#noRadio"
    output: str = ".mt-3"


class RadioLocator:
    yes_radio_button: Locator = (By.CSS_SELECTOR, RadioSelectors.yes_radio)
    impressive_radio_button: Locator = (By.CSS_SELECTOR, RadioSelectors.impressive_radio)
    no_radio_button: Locator = (By.CSS_SELECTOR, RadioSelectors.no_radio)
    output: Locator = (By.CSS_SELECTOR, RadioSelectors.output)


class RadioPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def goto(self):
        super().goto(URL.RADIO)

    def yes_radio_button(self):
        return base_element(self.driver, RadioLocator.yes_radio_button)

    def impressive_radio_button(self):
        return base_element(self.driver, RadioLocator.impressive_radio_button)

    def no_radio_button(self):
        return base_element(self.driver, RadioLocator.no_radio_button)

    def output(self):
        return base_element(self.driver, RadioLocator.output)
