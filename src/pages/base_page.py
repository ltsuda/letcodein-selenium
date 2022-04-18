import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base class for all web pages."""

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.waiter: WebDriverWait = WebDriverWait(self.driver, timeout=60)

    def goto(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def get_url(self) -> str:
        return self.driver.current_url

    def wait_until_url(self, url) -> bool:
        return self.waiter.until(EC.url_to_be(url))
