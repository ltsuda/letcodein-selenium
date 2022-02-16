import pytest


class TestSample:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.driver.get("https://letcode.in/edit")

    def test_sample_1(self):
        assert "Interact with Input fields" in self.driver.title

    def test_sample_2(self):
        assert "Interact with Input fields" in self.driver.title

    def test_sample_3(self):
        assert "Interact with Input fields" in self.driver.title

    def test_sample_4(self):
        assert "Interact with Input fields" in self.driver.title

    def test_sample_5(self):
        assert "Interact with Input fields" in self.driver.title
