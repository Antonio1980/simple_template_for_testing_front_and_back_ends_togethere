import allure
import pytest
from base.drivers.webdriver_factory import WebDriverFactory
from base.instruments.browser import Browser
from base.logger import automation_logger, logger
from tests.ui_tests.ui_tests_base.base_page import BasePage

test_case = "TestBasicScenario"


@allure.testcase(test_case)
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("web_driver")
@allure.description("""
    UI Parameterized Test run with Chrome and Firefox browsers.
    1. Simulate basic scenario with two players.
    """)
@pytest.mark.e2e
class TestBasicScenario(object):
    base_page = BasePage()

    @pytest.fixture()
    @automation_logger(logger)
    def web_driver(self, request):
        def stop_driver():
            logger.info("TEST STOP -> Closing browser... {0}".format(driver.name))
            Browser.close_browser(driver)

        logger.info("Driver is: {0}".format(request.param))
        driver = WebDriverFactory.get_driver(request.param)
        request.cls.driver = driver
        request.addfinalizer(stop_driver)
        return driver

    @automation_logger(logger)
    @pytest.mark.parametrize("web_driver", ["Chrome", "Firefox", ], indirect=True)
    def test_basic_scenario(self, web_driver):
        allure.step("Start playing.")
        result = self.base_page.open_base_page(web_driver)
        assert result is True

        cell1 = self.base_page.find_element(web_driver, self.base_page.locators.BOARD_ROWS + "[2]/button[2]")
        self.base_page.click_on_element(cell1)

        cell2 = self.base_page.find_element(web_driver, self.base_page.locators.BOARD_ROWS + "[3]/button[3]")
        self.base_page.click_on_element(cell2)

        cell3 = self.base_page.find_element(web_driver, self.base_page.locators.BOARD_ROWS + "[3]/button[2]")
        self.base_page.click_on_element(cell3)

        cell4 = self.base_page.find_element(web_driver, self.base_page.locators.BOARD_ROWS + "[2]/button[3]")
        self.base_page.click_on_element(cell4)

        cell5 = self.base_page.find_element(web_driver, self.base_page.locators.BOARD_ROWS + "[1]/button[2]")
        self.base_page.click_on_element(cell5)

        result = self.base_page.wait_element_clickable(web_driver, cell5, 5.0)
        assert result is False

        logger.info(F"============ TEST CASE {test_case} PASSED ===========")
