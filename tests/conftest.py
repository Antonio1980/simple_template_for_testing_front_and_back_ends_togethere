import time
import pytest
from base.drivers.webdriver_factory import WebDriverFactory
from base.instruments.api_client import ApiClient
from base.instruments.browser import Browser
from base.logger import automation_logger, logger


@pytest.fixture(scope="class")
@automation_logger(logger)
def r_time_count(request):
    start_time = time.perf_counter()
    logger.info("START TIME: {0}".format(start_time))

    def stop_counter():
        end_time = time.perf_counter()
        logger.info(F"END TIME: {end_time}")
        average_time = time.strptime(time.ctime(end_time - start_time), "%a %b %d %H:%M:%S %Y")
        min_ = average_time.tm_min
        sec_ = average_time.tm_sec
        logger.info("AVERAGE OF THE TEST CASE RUN TIME: {0} minutes {1} seconds".format(min_, sec_))

    request.addfinalizer(stop_counter)


@pytest.fixture()
@automation_logger(logger)
def web_driver(request):

    def stop_driver():
        logger.info("TEST STOP -> Closing browser... {0}".format(driver.name))
        Browser.close_browser(driver)

    logger.info("Driver is: {0}".format(request.param))
    driver = WebDriverFactory.get_driver(request.param)
    request.cls.driver = driver
    request.addfinalizer(stop_driver)
    return driver


@pytest.fixture(scope="class")
@automation_logger(logger)
def api_client():
    return ApiClient()
