import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from common.webelement import element


class TestSample:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://google.com")

    def test_sample_1(self):
        search_element = element(self.driver, (By.NAME, "q"))
        assert search_element.is_displayed()
