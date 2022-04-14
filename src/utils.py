from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Waiter:
    def __init__(self, driver: WebDriver, timeout: int = 60) -> None:
        self.driver: WebDriver = driver
        self.timeout: int = timeout
        self.waiter: WebDriverWait = WebDriverWait(self.driver, self.timeout)

    def wait(self, predicate: callable, until_not=True):
        wait_func: callable = self.waiter.until if until_not else self.waiter.until_not

        try:
            return wait_func(lambda _: predicate())
        except TimeoutException as exception:
            raise exception
