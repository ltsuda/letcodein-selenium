from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.consts import URL
from src.pages.base_page import BasePage
from src.webelement import Locator, base_element


class LinkSelectors:
    simple_link: str = "#simpleLink"
    dynamic_link: str = "#dynamicLink"
    created_link: str = "#created"
    no_content_link: str = "#no-content"
    moved_link: str = "#moved"
    bad_request_link: str = "#bad-request"
    unauthorized_link: str = "#unauthorized"
    forbidden_link: str = "#forbidden"
    not_found_link: str = "#invalid-url"
    output_response: str = "#linkResponse"


class LinkLocator:
    simple_link: Locator = (By.CSS_SELECTOR, LinkSelectors.simple_link)
    dynamic_link: Locator = (By.CSS_SELECTOR, LinkSelectors.dynamic_link)
    created_link: Locator = (By.CSS_SELECTOR, LinkSelectors.created_link)
    no_content_link: Locator = (By.CSS_SELECTOR, LinkSelectors.no_content_link)
    moved_link: Locator = (By.CSS_SELECTOR, LinkSelectors.moved_link)
    bad_request_link: Locator = (By.CSS_SELECTOR, LinkSelectors.bad_request_link)
    unauthorized_link: Locator = (By.CSS_SELECTOR, LinkSelectors.unauthorized_link)
    forbidden_link: Locator = (By.CSS_SELECTOR, LinkSelectors.forbidden_link)
    not_found_link: Locator = (By.CSS_SELECTOR, LinkSelectors.not_found_link)
    output_response: Locator = (By.CSS_SELECTOR, LinkSelectors.output_response)


class LinksPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def goto(self):
        super().goto(URL.LINKS)

    def simple_link(self):
        return base_element(self.driver, LinkLocator.simple_link)

    def dynamic_link(self):
        return base_element(self.driver, LinkLocator.dynamic_link)

    def created_link(self):
        return base_element(self.driver, LinkLocator.created_link)

    def no_content_link(self):
        return base_element(self.driver, LinkLocator.no_content_link)

    def moved_link(self):
        return base_element(self.driver, LinkLocator.moved_link)

    def bad_request_link(self):
        return base_element(self.driver, LinkLocator.bad_request_link)

    def unauthorized_link(self):
        return base_element(self.driver, LinkLocator.unauthorized_link)

    def forbidden_link(self):
        return base_element(self.driver, LinkLocator.forbidden_link)

    def not_found_link(self):
        return base_element(self.driver, LinkLocator.not_found_link)

    def output_response(self):
        return base_element(self.driver, LinkLocator.output_response)
