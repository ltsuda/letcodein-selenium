from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage


class ChekboxPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def goto(self):
        super().goto("https://demoqa.com/checkbox")
