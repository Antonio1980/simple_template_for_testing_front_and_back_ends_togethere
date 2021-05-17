from config_definitions import BaseConfig
from base.instruments.browser import Browser
from base.logger import automation_logger, logger
from tests.ui_tests.ui_tests_base.locators import base_page_locators


class BasePage(Browser):

    def __init__(self):
        super(Browser, self).__init__()
        self.base_url = BaseConfig.BASE_URL
        self.ui_delay = float(BaseConfig.UI_DELAY)
        self.locators = base_page_locators

    @automation_logger(logger)
    def open_base_page(self, driver):
        try:
            self.go_to_url(driver, self.base_url)
            return self.wait_url_contains(driver, self.base_url, self.ui_delay)
        except Exception as e:
            logger.error("{0} open_home_page failed with error: {1}".format(e.__class__.__name__,
                                                                            e.__cause__), e)
            return False
