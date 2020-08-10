import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from tests_base.enums import DriverHelper
from tests_base.logger import automation_logger, logger
from selenium.webdriver.support import expected_conditions as ec


class Browser:
    @classmethod
    @automation_logger(logger)
    def go_to_url(cls, driver, url):
        """
        Browse the given url by passed driver instance.
        :param driver: web_driver instance.
        :param url: string url to browse.
        :return: web_driver state.
        """
        driver.get(url)
        return driver.maximize_window()

    @classmethod
    @automation_logger(logger)
    def close_driver_instance(cls, driver):
        """
        Deletes all cookies and closes a browser.
        :param driver: web_driver instance.
        """
        driver.delete_all_cookies()
        driver.close()
        driver.quit()

    @classmethod
    @automation_logger(logger)
    def close_driver(cls, driver):
        """
        Closes browser page.
        :param driver: web_driver instance.
        """
        driver.close()

    @classmethod
    @automation_logger(logger)
    def close_browser(cls, driver):
        """
        Calling cls method to close driver instance.
        """
        cls.close_driver_instance(driver)

    @classmethod
    @automation_logger(logger)
    def driver_wait(cls, driver, delay):
        """
        Explicit wait for given driver with delay.
        :param delay: seconds to wait.
        :param driver: web_driver instance.
        :return: web_driver state.
        """
        return WebDriverWait(driver, delay)

    @classmethod
    @automation_logger(logger)
    def wait_driver(cls, driver, delay):
        """
        Implicit wait for given driver with delay.
        :param delay: seconds to wait.
        :param driver: web_driver instance.
        :return: web_driver state.
        """
        return driver.implicitly_wait(delay)

    @classmethod
    @automation_logger(logger)
    def get_cur_url(cls, driver):
        """
        Get the url from browser state.
        :param driver: web_driver instance.
        :return: current url from a browser.
        """
        return driver.current_url

    @classmethod
    @automation_logger(logger)
    def get_element_span_html(cls, element):
        """
        Get the innerHTML attribute value from a web element.
        :param element: web element.
        :return: string value of the innerHTML attribute.
        """
        return element.get_attribute("innerHTML")

    @classmethod
    @automation_logger(logger)
    def get_attribute_from_element(cls, element, attribute):
        """
        Get attribute text of a web element.
        :param element: web element.
        :param attribute: attribute string.
        :return: attribute value.
        """
        return element.get_attribute(attribute)

    @classmethod
    @automation_logger(logger)
    def get_attribute_from_locator(cls, driver, locator, attribute):
        """
        Get attribute of a web element.
        @param driver: WebDriver instance.
        @param locator: locator of web element.
        @param attribute: attribute string.
        :return: attribute value.
        """
        element = cls.find_element(driver, locator)
        return element.get_attribute(attribute)

    @classmethod
    @automation_logger(logger)
    def send_enter_key(cls, element):
        """
        Clicks on 'ENTER' button for given web element.
        :param element: web element.
        """
        element.send_keys(Keys.ENTER)

    @classmethod
    def open_new_tab(cls, driver):
        """
        Opens new blank browser tab.
        :param driver: web_driver instance.
        """
        driver.execute_script('window.open("about:blank", "_blank");')

    @classmethod
    @automation_logger(logger)
    def close_tab(cls, driver):
        """
        Closes the current open browser page.
        :param driver: web_driver instance.
        """
        try:
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        except TimeoutException as e:
            logger.error("{0} method close_tab failed with error {0}".format(e.__class__.__name__, e.__cause__),
                                e)

    @classmethod
    @automation_logger(logger)
    def execute_js(cls, driver, script, *args):
        """
        Injection js code into current driver state.
        :param args: tuple of additional_tests parameters.
        :param driver: web_driver instance.
        :param script: java script code passed as string.
        :return: result of the script execution.
        """
        return driver.execute_script(script, args)

    @classmethod
    @automation_logger(logger)
    def hover_over_element_and_click(cls, driver, element):
        """
        Hover over web element and clicks on it.
        :param driver: web_driver instance.
        :param element: web element.
        :return: browser state with performed actions.
        """
        action = Actions(driver)
        action.move_to_element(element)
        action.click(element)
        return action.perform()

    @classmethod
    @automation_logger(logger)
    def try_click(cls, driver, element, delay=1.0):
        """
        Clicks with time delay between actions.
        :param driver: web_driver instance.
        :param element: web element.
        :param delay: seconds to wait.
        :return: browser state with performed actions.
        """
        action = Actions(driver)
        action.move_to_element(element)
        action.wait(delay)
        action.click(element)
        action.wait(delay)
        return action.perform()

    @classmethod
    @automation_logger(logger)
    def refresh_page(cls, driver):
        """
        Refresh browser page by sending 'Ctrl + r' keys.
        :param driver: web_driver instance.
        """
        try:
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
        except TimeoutException as e:
            logger.exception(F"{e.__class__.__name__} method refresh_page failed with error {e}")

    @classmethod
    @automation_logger(logger)
    def refresh_browser(cls, driver):
        """
        Refresh browser by navigating on 'refresh' button.
        :param driver: web_driver instance.
        """
        driver.refresh()

    @classmethod
    @automation_logger(logger)
    def back_browser(cls, driver):
        """
        To go back on previous page using driver.
        :param driver: web_driver instance.
        """
        driver.navigate().back()

    @classmethod
    @automation_logger(logger)
    def forward_browser(cls, driver):
        """
        To go forward on previous page using driver.
        :param driver: web_driver instance.
        """
        driver.navigate().forward()

    @classmethod
    @automation_logger(logger)
    def go_back(cls, driver):
        """
        To go back on previous page using js.
        :param driver: web_driver instance.
        """
        driver.execute_script("window.history.go(-1)")

    @classmethod
    @automation_logger(logger)
    def select_by_value(cls, element, value):
        """
        Select option from selector by value.
        :param element: selector web element.
        :param value: value for option to select.
        """
        if value is not str:
            value = str(value)
        selector = Select(element)
        selector.select_by_value(value)

    @classmethod
    @automation_logger(logger)
    def select_by_index(cls, element, index):
        """
        Select option from selector by index.
        :param element: selector web element.
        :param index: value for option to select.
        """
        if index is not int:
            index = int(index)
        selector = Select(element)
        selector.select_by_index(index)

    @classmethod
    @automation_logger(logger)
    def send_keys(cls, element, query):
        """
        Clear and type a text into web element.
        :param element: web element.
        :param query: text to type.
        """
        element.clear()
        element.send_keys(query)

    @classmethod
    @automation_logger(logger)
    def clear_field(cls, element):
        """
        Clear input field.
        :param element: web element.
        """
        element.clear()

    @classmethod
    @automation_logger(logger)
    def get_attribute_from_locator(cls, driver, locator, attribute):
        """
        Get attribute text of a web element by locator.
        :param driver: web_driver instance.
        :param locator: locator string.
        :param attribute: attribute string.
        :return: attribute value.
        """
        element = cls.find_element(driver, locator)
        return element.get_attribute(attribute)

    @classmethod
    @automation_logger(logger)
    def search_element(cls, driver, locator, delay):
        """
        Search a web element on a page.
        :param driver: web_driver instance.
        :param delay: seconds to wait an element.
        :param locator: xpath of a element.
        :return: web element.
        """
        try:
            return cls.driver_wait(driver, delay).until(lambda x: x.find_element_by_xpath(locator))
        except TimeoutException as e:
            logger.error(F"{e.__class__.__name__} search_element raising error: {e}")
            return False

    @classmethod
    @automation_logger(logger)
    def input_data(cls, element, data):
        """
        Type text into a field
        :param element: web element.
        :param data: text to type.
        """
        element.clear()
        element.send_keys(data)
        element.send_keys(Keys.ENTER)

    @classmethod
    @automation_logger(logger)
    def type_text_by_locator(cls, driver, locator, query):
        """
        Clear and type text into web element.
        :param driver: web_driver instance.
        :param locator: xpath of a element.
        :param query: text to type.
        """
        delay = 5
        element = cls.search_element(driver, locator, delay)
        element.click()
        element.clear()
        element.send_keys(query)
        cls.send_enter_key(element)

    @classmethod
    @automation_logger(logger)
    def click_on_element_by_locator(cls, driver, locator, delay):
        """
        Wait, search by locator and click on a web element.
        :param driver: web_driver instance.
        :param delay: seconds to wait an element.
        :param locator: xpath of a element.
        """
        try:
            cls.wait_element_clickable(driver, locator, delay).click()
        except AttributeError as e:
            logger.error(F"{e.__class__.__name__} click_on_element_by_locator raising error: {e}")
            raise e

    @classmethod
    @automation_logger(logger)
    def click_on_element(cls, element):
        """
        Click on a passed web element.
        :param element: web element.
        """
        element.click()

    @classmethod
    @automation_logger(logger)
    def check_element_is_not_presented(cls, driver, locator):
        """
        Check than element not presented on the page.
        :param driver: web_driver instance.
        :param locator: xpath of a element.
        :return: web element if element visible and False otherwise.
        """
        try:
            driver.find_element_by_xpath(locator)
        except NoSuchElementException as e:
            logger.error(F"{e.__class__.__name__} check_element_is_not_presented raising error: {e}")
            return True
        return False

    @classmethod
    @automation_logger(logger)
    def check_element_not_presented(cls, driver, locator, delay):
        """
        Wait and check than element not present on the page.
        :param driver: web_driver instance.
        :param delay: seconds to wait an element.
        :param locator: xpath of a element.
        :return: web element if element presented and False otherwise.
        """
        try:
            return cls.driver_wait(driver, delay).until_not(ec.presence_of_element_located((By.XPATH, locator)))
        except TimeoutException as e:
            logger.error(F"{e.__class__.__name__} check_element_not_presented raising error: {e}")
            return False

    @classmethod
    @automation_logger(logger)
    def check_element_to_not_be_selected(cls, driver, locator, delay):
        """
        Wait for element to be click able on the page.
        :param driver: web_driver instance.
        :param delay: seconds to wait an element.
        :param locator: xpath of a element.
        :return: web element if element can be selected and False otherwise.
        """
        try:
            return cls.driver_wait(driver, delay).until_not(ec.element_to_be_selected((By.XPATH, locator)))
        except TimeoutException as e:
            logger.error(F"{e.__class__.__name__} check_element_to_not_be_selected raising error: {e}")
            return False

    @classmethod
    @automation_logger(logger)
    def wait_url_contains(cls, driver, url, delay):
        """
        Waits and checks if expected url is contains to current url.
        :param driver: web_driver instance.
        :param delay: seconds to wait an element.
        :param url: expected url.
        :return: True if matches condition and False otherwise.
        """
        try:
            return cls.driver_wait(driver, delay).until(ec.url_contains(url))
        except TimeoutException as e:
            logger.error(F"{e.__class__.__name__} wait_url_contains raising error: {e}")
            return False

    @classmethod
    @automation_logger(logger)
    def wait_url_matches(cls, driver, url, delay):
        """
        Waits and checks if expected url is matches to current url.
        :param driver: web_driver instance.
        :param delay: seconds to wait an element.
        :param url: expected url.
        :return: True if matches condition and False otherwise.
        """
        try:
            return cls.driver_wait(driver, delay).until(ec.url_matches(url))
        except TimeoutException as e:
            logger.error(F"{e.__class__.__name__} wait_url_matches raising error: {e}")
            return False

    @classmethod
    @automation_logger(logger)
    def wait_element_visible(cls, driver, locator, delay):
        """
        Wait for element to be visible on the page.
        :param driver: web_driver instance.
        :param delay: seconds to wait an element.
        :param locator: xpath of a element.
        :return: web element.
        """
        try:
            return cls.driver_wait(driver, delay).until(ec.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException as e:
            logger.error(F"{e.__class__.__name__} wait_element_visible raising error: {e}")
            return False

    @classmethod
    @automation_logger(logger)
    def wait_element_presented(cls, driver, locator, delay):
        """
        Wait for element to be presented on the page.
        :param driver: web_driver instance.
        :param delay: seconds to wait an element.
        :param locator: xpath of a element.
        :return: web element.
        """
        try:
            return cls.driver_wait(driver, delay).until(ec.presence_of_element_located((By.XPATH, locator)))
        except TimeoutException as e:
            logger.error(F"{e.__class__.__name__} wait_element_presented raising error: {e}")
            return False

    @classmethod
    @automation_logger(logger)
    def wait_element_to_be_selected(cls, driver, locator, delay):
        """
        Wait for element to be click able on the page.
        :param driver: web_driver instance.
        :param delay: seconds to wait an element.
        :param locator: xpath of a element.
        :return: web element.
        """
        try:
            return cls.driver_wait(driver, delay).until(ec.element_to_be_selected((By.XPATH, locator)))
        except TimeoutException as e:
            logger.error(F"{e.__class__.__name__} wait_element_to_be_selected raising error: {e}")
            return False

    @classmethod
    @automation_logger(logger)
    def wait_element_clickable(cls, driver, locator, delay):
        """
        Wait for element to be click able on the page.
        :param driver: web_driver instance.
        :param delay: seconds to wait an element.
        :param locator: xpath of a element.
        :return: web element.
        """
        try:
            return cls.driver_wait(driver, delay).until(ec.element_to_be_clickable((By.XPATH, locator)))
        except Exception as e:
            logger.error(F"{e.__class__.__name__} wait_element_clickable raising error: {e}")
            return False

    @classmethod
    @automation_logger(logger)
    def find_element(cls, driver, locator):
        """
        Find a web element without waiting by locator.
        :param driver: web_driver instance.
        :param locator: xpath of a element.
        :return: web element.
        """
        return driver.find_element_by_xpath(locator)

    @classmethod
    @automation_logger(logger)
    def find_element_by(cls, driver, locator, by):
        """
        Find a web element by provided option.
        :param driver: web_driver instance.
        :param locator: xpath of a element.
        :param by: selenium option to search web element.
        :return: web element.
        """
        by = by.lower()
        try:
            if by == DriverHelper.ID.value:
                return driver.find_element(By.ID, locator)
            elif by == DriverHelper.NAME.value:
                return driver.find_element(By.NAME, locator)
            elif by == DriverHelper.CLASS_NAME.value:
                return driver.find_element(By.CLASS_NAME, locator)
            elif by == DriverHelper.TAG_NAME.value:
                return driver.find_element(By.TAG_NAME, locator)
            elif by == DriverHelper.LINK_TEXT.value:
                return driver.find_element(By.LINK_TEXT, locator)
            elif by == DriverHelper.CSS_SELECTOR.value:
                return driver.find_element(By.CSS_SELECTOR)
            elif by == DriverHelper.PARTIAL_LINK_TEXT.value:
                return driver.find_element(By.PARTIAL_LINK_TEXT, locator)
            else:
                return driver.find_element(By.XPATH, locator)
        except Exception as e:
            logger.error(e)
            return False

    @classmethod
    @automation_logger(logger)
    def find_elements(cls, driver, locator):
        """
        Find all duplicated elements in a DOM.
        :param driver: web_driver instance.
        :param locator: selector web element.
        :return: list of web elements.
        """
        return [i for i in driver.find_elements_by_xpath(locator)]


class Actions(ActionChains):
    def wait(self, delay: float):
        self._actions.append(lambda: time.sleep(delay))
        return self
