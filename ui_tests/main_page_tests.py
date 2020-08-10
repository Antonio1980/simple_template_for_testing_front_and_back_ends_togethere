import allure
import pytest
from tests_base.logger import automation_logger, logger
from ui_tests.ui_tests_base.base_page import BasePage

test_case = "TestMainPage"


@allure.testcase(test_case)
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("web_driver")
@allure.description("""
    UI Test.
    1. Check that default title of the main exists and presented.
    2. Verify that "New Game" button located under the title, having red color and clickable.
    """)
@pytest.mark.ui
class TestMainPage(object):
    base_page = BasePage()

    @automation_logger(logger)
    def test_default_title(self, web_driver):
        allure.step("Check the default title.")
        result = self.base_page.open_base_page(web_driver)
        assert result is True
        title = self.base_page.get_attribute_from_locator(web_driver, self.base_page.locators.TITLE, "innerHTML")
        assert "Next player: X" == title

        logger.info(F"============ TEST CASE {test_case} / 1 PASSED ===========")

    @automation_logger(logger)
    def test_new_game_button(self, web_driver):
        allure.step("Check 'New game' button.")
        result = self.base_page.open_base_page(web_driver)
        assert result is True
        button = self.base_page.find_element(web_driver, self.base_page.locators.NEW_GAME)
        assert "React App" == button.parent.title

        logger.info(F"============ TEST CASE {test_case} / 2 PASSED ===========")
