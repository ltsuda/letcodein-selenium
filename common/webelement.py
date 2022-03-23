from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Selenium locator (By.identifier, 'selector')
Locator = tuple[By, str]


class BaseWebElement:
    """Base class for all web objects."""

    def __init__(self, driver: WebDriver, locator: Locator = None, timeout: int = 60):
        self.driver: WebDriver = driver
        if locator is not None and isinstance(locator, tuple):
            self.locator: Locator = locator
        else:
            raise Exception(
                "Locator is not defined." "Please enter 'locator=(By.<identifier>, <str>)'"
            )
        self.timeout: int = timeout
        self.wait: WebDriverWait = WebDriverWait(driver, self.timeout)
        self.element: WebElement | None = None
        self.select_object: Select | None = None

    def _wait_for(self, to_find: bool = True):
        """Wait for element to be found or not

        1 - valid selector + wait until -> assign element to element class propertie
        2 - valid selector + wait until_not -> raises timeout exception if element still present
        3 - invalid selector + wait until -> raises timeout exception if element still present
        4 - invalid selector + wait until_not -> try wait resolves to True, so it does nothing

        Args:
            to_find (bool, optional): whether wait to find or not the element. Defaults to True.

        Raises:
            exception: TimeoutException for finding or not finding element

        Returns:
            self (BaseWebElement): instance class
        """
        wait_func: callable = self.wait.until if to_find else self.wait.until_not

        try:
            element: WebElement = wait_func(lambda _: self.driver.find_element(*self.locator))
        except TimeoutException as exception:
            raise exception
        else:
            if to_find:
                self.element: WebElement = element
            return self

    def clear(self):
        self._wait_for(to_find=True).element.clear()
        return self

    def click(self):
        self._wait_for(to_find=True).element.click()
        return self

    def find_element(self, locator: Locator, to_find: bool = True):
        self.locator = locator
        self.element = self._wait_for(to_find=to_find).element
        return self

    def find_elements(self, locator: Locator):
        # TODO: return find_elements directly or create a BaseWebElement class for list of elements
        pass

    def screenshot(self, filename: str):
        self._wait_for(to_find=True).element.screenshot(filename)
        return self

    def send_keys(self, *value):
        self._wait_for(to_find=True).element.send_keys(*value)
        return self

    # Select

    def _get_select_object(self):
        self.select_object = Select(self._wait_for(to_find=True).element)
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

    # Information

    def get_attribute(self, name: str) -> str | None | bool:
        return self._wait_for(to_find=True).element.get_attribute(name)

    def get_dom_attribute(self, name: str) -> str | None | bool:
        return self._wait_for(to_find=True).element.get_dom_attribute(name)

    def get_property(self, name: str) -> str | None | bool:
        return self._wait_for(to_find=True).element.get_property(name)

    def is_displayed(self) -> bool:
        return self._wait_for(to_find=True).element.is_displayed()

    def is_enabled(self) -> bool:
        return self._wait_for(to_find=True).element.is_enabled()

    def is_selected(self) -> bool:
        return self._wait_for(to_find=True).element.is_selected()

    def location(self) -> dict:
        return self._wait_for(to_find=True).element.location

    def location_once_scrolled_into_view(self) -> dict:
        return self._wait_for(to_find=True).element.location_once_scrolled_into_view

    def parent(self):
        return self._wait_for(to_find=True).element.parent

    def screenshot_as_base64(self) -> str:
        return self._wait_for(to_find=True).element.screenshot_as_base64

    def screenshot_as_png(self) -> str:
        return self._wait_for(to_find=True).element.screenshot_as_png

    def size(self) -> dict:
        return self._wait_for(to_find=True).element.size

    def tag_name(self) -> str:
        return self._wait_for(to_find=True).element.tag_name

    def rect(self) -> dict:
        return self._wait_for(to_find=True).element.rect

    def value_of_css_property(self, property: str) -> str:
        return self._wait_for(to_find=True).element.value_of_css_property(property)

    def text(self) -> str:
        return self._wait_for(to_find=True).element.text
