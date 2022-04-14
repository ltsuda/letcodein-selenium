import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from src.consts import URL
from src.pages.elements.links.links_page import LinksPage
from src.utils import Waiter


class TestLinks:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.links_page = LinksPage(driver)
        self.links_page.goto()
        self.links_page.wait_until_url(URL.LINKS)
        self.waiter = Waiter(driver)

    def test_simple_link(self):
        main_window = self.links_page.driver.current_window_handle
        window_handles = self.links_page.driver.window_handles

        self.links_page.simple_link().click()

        # TODO: why self.waiter.wait(EC.new_window_is_opened(window_handles)) doesn't work
        # with missing predicate driver error
        assert self.waiter.waiter.until(EC.new_window_is_opened(window_handles))

        windows = self.links_page.driver.window_handles
        windows.remove(main_window)
        self.links_page.driver.switch_to.window(windows[0])

        assert self.links_page.wait_until_url(URL.HOME)

    def test_dynamic_link(self):
        main_window = self.links_page.driver.current_window_handle
        window_handles = self.links_page.driver.window_handles

        self.links_page.dynamic_link().click()

        # TODO: why self.waiter.wait(EC.new_window_is_opened(window_handles)) doesn't work
        # with missing predicate driver error
        assert self.waiter.waiter.until(EC.new_window_is_opened(window_handles))

        windows = self.links_page.driver.window_handles
        windows.remove(main_window)
        self.links_page.driver.switch_to.window(windows[0])

        assert self.links_page.wait_until_url(URL.HOME)

    def test_created_link(self):
        expected_response = "Link has responded with staus 201 and status text Created"
        self.links_page.created_link().click()
        assert self.links_page.output_response().element_text_is(expected_response)

    def test_no_content_link(self):
        expected_response = "Link has responded with staus 204 and status text No Content"
        self.links_page.no_content_link().click()
        assert self.links_page.output_response().element_text_is(expected_response)

    def test_moved_link(self):
        expected_response = "Link has responded with staus 301 and status text Moved Permanently"
        self.links_page.moved_link().click()
        assert self.links_page.output_response().element_text_is(expected_response)

    def test_bad_request_link(self):
        expected_response = "Link has responded with staus 400 and status text Bad Request"
        self.links_page.bad_request_link().click()
        assert self.links_page.output_response().element_text_is(expected_response)

    def test_unauthorized_link(self):
        expected_response = "Link has responded with staus 401 and status text Unauthorized"
        self.links_page.unauthorized_link().click()
        assert self.links_page.output_response().element_text_is(expected_response)

    def test_forbidden_link(self):
        expected_response = "Link has responded with staus 403 and status text Forbidden"
        self.links_page.forbidden_link().click()
        assert self.links_page.output_response().element_text_is(expected_response)

    def test_not_found_link(self):
        expected_response = "Link has responded with staus 404 and status text Not Found"
        self.links_page.not_found_link().click()
        assert self.links_page.output_response().element_text_is(expected_response)
