import time
import pytest
from tests_base.drivers.webdriver_factory import WebDriverFactory
from tests_base.instruments.api_client import ApiClient
from tests_base.instruments.browser import Browser
from tests_base.logger import automation_logger, logger


@pytest.fixture(scope="class")
@automation_logger(logger)
def r_time_count(request):
    start_time = time.perf_counter()
    print("START TIME: {0}".format(start_time))

    def stop_counter():
        end_time = time.perf_counter()
        print(F"END TIME: {end_time}")
        average_time = time.strptime(time.ctime(end_time - start_time), "%a %b %d %H:%M:%S %Y")
        min_ = average_time.tm_min
        sec_ = average_time.tm_sec
        print("AVERAGE OF THE TEST CASE RUN TIME: {0} minutes {1} seconds".format(min_, sec_))

    request.addfinalizer(stop_counter)


@pytest.fixture(scope="class", params=[["chrome"]])
@automation_logger(logger)
def web_driver(request):

    def stop_driver():
        logger.info("TEST STOP -> Closing browser... {0}".format(web_driver.name))
        Browser.close_browser(web_driver)

    logger.info("Driver is: {0}".format(request.param[0]))
    web_driver = WebDriverFactory.get_driver(request.param[0])
    request.cls.driver = web_driver
    request.addfinalizer(stop_driver)
    return web_driver


@pytest.fixture(scope="class")
@automation_logger(logger)
def api_client():
    return ApiClient()
