from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.webelement import base_element


class TestLinks:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get("https://demoqa.com/links")

        # elements
        self.simple_link = base_element(self.driver, (By.CSS_SELECTOR, "#simpleLink"))
        self.dynamic_link = base_element(self.driver, (By.CSS_SELECTOR, "#dynamicLink"))
        self.created_link = base_element(self.driver, (By.CSS_SELECTOR, "#created"))
        self.no_content_link = base_element(self.driver, (By.CSS_SELECTOR, "#no-content"))
        self.moved_link = base_element(self.driver, (By.CSS_SELECTOR, "#moved"))
        self.bad_request_link = base_element(self.driver, (By.CSS_SELECTOR, "#bad-request"))
        self.unauthorized_link = base_element(self.driver, (By.CSS_SELECTOR, "#unauthorized"))
        self.forbidden_link = base_element(self.driver, (By.CSS_SELECTOR, "#forbidden"))
        self.not_found_link = base_element(self.driver, (By.CSS_SELECTOR, "#invalid-url"))
        self.output_response = base_element(self.driver, (By.CSS_SELECTOR, "#linkResponse"))

        # variable
        self.home_url = "https://demoqa.com/"

    def test_simple_link(self):
        main_window = self.driver.current_window_handle
        window_handles = self.driver.window_handles

        self.simple_link.click()

        assert self.wait.until(EC.new_window_is_opened(window_handles))

        windows = self.driver.window_handles
        windows.remove(main_window)
        self.driver.switch_to.window(windows[0])

        assert self.wait.until(EC.url_to_be(self.home_url))

    def test_dynamic_link(self):
        main_window = self.driver.current_window_handle
        window_handles = self.driver.window_handles

        self.dynamic_link.click()

        assert self.wait.until(EC.new_window_is_opened(window_handles))

        windows = self.driver.window_handles
        windows.remove(main_window)
        self.driver.switch_to.window(windows[0])

        assert self.wait.until(EC.url_to_be(self.home_url))

    def test_created_link(self):
        expected_response = "Link has responded with staus 201 and status text Created"
        self.created_link.click()
        assert self.output_response.text() == expected_response

    def test_no_content_link(self):
        expected_response = "Link has responded with staus 204 and status text No Content"
        self.no_content_link.click()
        assert self.output_response.text() == expected_response

    def test_moved_link(self):
        expected_response = "Link has responded with staus 301 and status text Moved Permanently"
        self.moved_link.click()
        assert self.output_response.text() == expected_response

    def test_bad_request_link(self):
        expected_response = "Link has responded with staus 400 and status text Bad Request"
        self.bad_request_link.click()
        assert self.output_response.text() == expected_response

    def test_unauthorized_link(self):
        expected_response = "Link has responded with staus 401 and status text Unauthorized"
        self.unauthorized_link.click()
        assert self.output_response.text() == expected_response

    def test_forbidden_link(self):
        expected_response = "Link has responded with staus 403 and status text Forbidden"
        self.forbidden_link.click()
        assert self.output_response.text() == expected_response

    def test_not_found_link(self):
        expected_response = "Link has responded with staus 404 and status text Not Found"
        self.not_found_link.click()
        assert self.output_response.text() == expected_response
