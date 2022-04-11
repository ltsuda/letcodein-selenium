import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.webelement import base_element


class TestCheckbox:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://demoqa.com/checkbox")

        # variables
        self.dir_list = [
            "home",
            "desktop",
            "notes",
            "commands",
            "documents",
            "workspace",
            "react",
            "angular",
            "veu",
            "office",
            "public",
            "private",
            "classified",
            "general",
            "downloads",
            "wordFile",
            "excelFile",
        ]

        # selector
        self.toggle_selector = "[aria-label='Toggle']"
        self.open_icon_selector = "{} svg.rct-icon-expand-open".format(self.toggle_selector)
        self.close_icon_selector = "{} svg.rct-icon-expand-close".format(self.toggle_selector)
        self.result = "#result"
        self.result_prefix = "{} span".format(self.result)
        self.result_text = "{} .text-success".format(self.result)
        self.checked_selector = ".rct-checkbox .rct-icon-check"
        self.unchecked_selector = ".rct-checkbox .rct-icon-uncheck"
        self.half_checked_selector = ".rct-checkbox .rct-icon-half-check"

        # elements
        self.expand_all_button = base_element(
            self.driver, (By.CSS_SELECTOR, "[aria-label='Expand all']")
        )
        self.collapse_all_button = base_element(
            self.driver, (By.CSS_SELECTOR, "[aria-label='Collapse all']")
        )
        self.toggle_button = base_element(self.driver, (By.CSS_SELECTOR, self.toggle_selector))
        self.open_button = base_element(self.driver, (By.CSS_SELECTOR, self.open_icon_selector))
        self.close_button = base_element(self.driver, (By.CSS_SELECTOR, self.close_icon_selector))
        self.home_button = base_element(
            self.driver, (By.CSS_SELECTOR, "label[for='tree-node-home']")
        )
        self.checked = base_element(self.driver, (By.CSS_SELECTOR, self.checked_selector))
        self.unchecked = base_element(self.driver, (By.CSS_SELECTOR, self.unchecked_selector))
        self.half_checked = base_element(
            self.driver, (By.CSS_SELECTOR, self.half_checked_selector)
        )
        self.selected_prefix = base_element(self.driver, (By.CSS_SELECTOR, self.result_prefix))
        self.result_element = base_element(self.driver, (By.CSS_SELECTOR, self.result_text))

    def test_expand_and_collapse_all(self):
        self.expand_all_button.click()
        assert self.close_button.element_is_not_present()

        self.collapse_all_button.click()
        assert self.open_button.element_is_not_present()

    def test_select_all(self):
        self.expand_all_button.click()
        self.home_button.click()

        assert self.selected_prefix.is_displayed()

        selected_items = self.result_element.find_elements()
        assert len(self.dir_list) == len(selected_items)

        for item in selected_items:
            text = item.text
            assert text in self.dir_list

        assert self.unchecked.element_is_not_present()

    def test_unselect_all(self):
        self.expand_all_button.click()
        self.home_button.click()
        self.home_button.click()

        assert self.selected_prefix.element_is_not_present()
        assert self.checked.element_is_not_present()
