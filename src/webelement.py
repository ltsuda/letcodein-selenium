from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.select import Select

from src.utils import Waiter

# Selenium locator (By.identifier, 'selector')
Locator = tuple[By, str]


def base_element(
    driver: WebDriver, locator: Locator = None, element: WebElement = None, timeout: int = 15
):
    return BaseWebElement(driver, locator, element, timeout)


class BaseWebElement:
    """Base class for all web objects."""

    def __init__(
        self,
        driver: WebDriver,
        locator: Locator = None,
        element: WebElement = None,
        timeout: int = 60,
    ):
        self.driver: WebDriver = driver
        self.element: WebElement | None = None
        if locator is not None and isinstance(locator, tuple) and element is None:
            self.locator: Locator = locator
        elif element is not None and locator is None:
            self.element: WebElement = element
        elif element is not None and locator is not None and isinstance(locator, tuple):
            self.element: WebElement = element
            self.locator: Locator = locator
        else:
            raise Exception(
                "Locator is not defined."
                "Please enter 'locator=(By.<identifier>, <str>)'"
                "Element is not defined."
                "Please enter 'element' of type WebElement"
            )
        self.timeout: int = timeout
        self.waiter: Waiter = Waiter(self.driver, self.timeout)
        self.action: ActionChains = ActionChains(self.driver)
        self.select_object: Select | None = None

    def wait_for_element(self):
        def _predicate():
            return self.driver.find_element(*self.locator)

        self.element = self.waiter.wait(_predicate)
        return self

    def wait_for_elements(self):
        def _predicate():
            return self.find_elements()

        return self.waiter.wait(_predicate)

    def clear(self):
        self.wait_for_element().element.clear()
        return self

    def click(self):
        self.wait_for_element().element.click()
        return self

    def find_child_element(self, locator: Locator):
        def _predicate():
            return self.wait_for_element().element.find_element(*locator)

        return base_element(self.driver, locator, element=self.waiter.wait(_predicate))

    def find_elements(self):
        return self.driver.find_elements(*self.locator)

    def screenshot(self, filename: str):
        self.wait_for_element().element.screenshot(filename)
        return self

    def send_keys(self, *value):
        self.wait_for_element().element.send_keys(*value)
        return self

    # Select

    def _get_select_object(self):
        self.select_object = Select(self.wait_for_element().element)
        return self

    def all_selected_options(self) -> list:
        return self._get_select_object().select_object.all_selected_options

    def deselect_all(self):
        self._get_select_object().select_object.deselect_all()
        return self

    def deselect_by_index(self, index: int):
        self._get_select_object().select_object.deselect_by_index(index)
        return self

    def deselect_by_value(self, value: str):
        self._get_select_object().select_object.deselect_by_value(value)
        return self

    def deselect_by_visible_text(self, text: str):
        self._get_select_object().select_object.deselect_by_visible_text(text)
        return self

    def first_selected_option(self):
        return self._get_select_object().select_object.first_selected_option

    def options(self):
        return self._get_select_object().select_object.options

    def select_by_index(self, index: int):
        self._get_select_object().select_object.select_by_index(index)
        return self

    def select_by_value(self, value: str):
        self._get_select_object().select_object.select_by_value(value)
        return self

    def select_by_visible_text(self, text: str):
        self._get_select_object().select_object.select_by_visible_text(text)
        return self

    # # Information

    def get_attribute(self, name: str) -> str | None | bool:
        return self.wait_for_element().element.get_attribute(name)

    def get_dom_attribute(self, name: str) -> str | None | bool:
        return self.wait_for_element().element.get_dom_attribute(name)

    def get_property(self, name: str) -> str | None | bool:
        return self.wait_for_element().element.get_property(name)

    def is_displayed(self) -> bool:
        return self.wait_for_element().element.is_displayed()

    def is_enabled(self) -> bool:
        return self.wait_for_element().element.is_enabled()

    def is_selected(self) -> bool:
        return self.wait_for_element().element.is_selected()

    def location(self) -> dict:
        return self.wait_for_element().element.location

    def location_once_scrolled_into_view(self) -> dict:
        return self.wait_for_element().element.location_once_scrolled_into_view

    def parent(self):
        return self.wait_for_element().element.parent

    def screenshot_as_base64(self) -> str:
        return self.wait_for_element().element.screenshot_as_base64

    def screenshot_as_png(self) -> str:
        return self.wait_for_element().element.screenshot_as_png

    def size(self) -> dict:
        return self.wait_for_element().element.size

    def tag_name(self) -> str:
        return self.wait_for_element().element.tag_name

    def rect(self) -> dict:
        return self.wait_for_element().element.rect

    def value_of_css_property(self, property: str) -> str:
        return self.wait_for_element().element.value_of_css_property(property)

    def text(self) -> str:
        return self.wait_for_element().element.text

    # expect

    def element_text_is(self, expected: str) -> bool:
        text = self.text()
        return expected == text

    def contain_text(self, expected: str) -> bool:
        text = self.text()
        return expected in text

    def element_is_present(self) -> bool:
        try:
            self.driver.find_element(*self.locator)
        except NoSuchElementException:
            return False
        else:
            return True

    def element_is_not_present(self) -> bool:
        return self.element_is_present() == False

    def elements_are_present(self) -> bool:
        elements = self.driver.find_elements(*self.locator)
        return len(elements) > 1

    def elements_are_not_present(self) -> bool:
        elements = self.driver.find_elements(*self.locator)
        return len(elements) == 0

    def contain_class(self, expected: str) -> bool:
        classes = self.get_attribute("class")
        return expected in classes

    # wait and expect

    def wait_until_element_is_present(self) -> bool:
        return len(self.wait_for_elements()) == 1

    def wait_until_element_is_not_present(self) -> bool:
        return len(self.wait_for_elements()) == 0

    def wait_until_elements_are_present(self) -> bool:
        return len(self.wait_for_elements()) > 1

    # actions

    def double_click(self):
        self.wait_for_element().action.double_click(on_element=self.element)
        self.action.perform()
        return self

    def right_click(self):
        self.wait_for_element().action.context_click(on_element=self.element)
        self.action.perform()
        return self
