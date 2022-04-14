from selenium.webdriver.remote.webdriver import WebDriver

from src.utils import Waiter


class BasePage:
    """Base class for all web pages."""

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.waiter: Waiter = Waiter(self.driver)

    def goto(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def get_url(self) -> str:
        return self.driver.current_url

    def wait_until_url(self, url) -> bool:
        def _predicate():
            return self.get_url() == url

        return self.waiter.wait(_predicate)
