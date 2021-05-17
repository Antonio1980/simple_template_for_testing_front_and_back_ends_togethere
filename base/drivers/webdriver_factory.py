import subprocess
import multiprocessing
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from testcontainers.selenium import BrowserWebDriverContainer

from config_definitions import BaseConfig
from base.automation_error import AutomationError
from base.enums import Browsers, OperationSystem
from base.logger import logger, automation_logger
from base.utils.utils import Utils


class WebDriverFactory:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--enable-benchmarking')
    # chrome_options.add_argument('--enable-net-benchmarking')
    # chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_experimental_option('w3c', False)

    opera_options = webdriver.ChromeOptions()
    opera_options.binary_location = BaseConfig.M_OPERA_PATH

    @classmethod
    @automation_logger(logger)
    def get_driver(cls, browser_name=None):
        """
        Define Operational System and return driver accordingly.
        :param browser_name: Chrome, Firefox, Edge or IE
        :return: web driver.
        """
        browser_name = browser_name.lower()
        if browser_name is None:
            browser_name = Browsers.CHROME.value
        if Utils.detect_os() == OperationSystem.WINDOWS.value:
            return cls.get_driver_win(browser_name)
        elif Utils.detect_os() == OperationSystem.DARWIN.value:
            return cls.get_driver_mac(browser_name)
        elif Utils.detect_os() == OperationSystem.LINUX.value:
            return cls.get_driver_lin(browser_name)
        else:
            error = "Operational System not detected."
            logger.error(error)
            raise AutomationError(error)

    @classmethod
    @automation_logger(logger)
    def get_driver_win(cls, browser_name):
        """
        Choose needed driver according to Windows OS.
        :param browser_name: Chrome, Firefox, Edge or IE
        :return: web driver.
        """
        if browser_name == Browsers.FIREFOX.value:
            try:
                return webdriver.Firefox(executable_path=GeckoDriverManager().install())
            except Exception as e:
                print(e)
                return webdriver.Firefox(executable_path=BaseConfig.W_FIREFOX_PATH)
        elif browser_name == Browsers.CHROME.value:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option('w3c', False)
            try:
                return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
            except Exception as e:
                logger.exception(e)
                return webdriver.Chrome(executable_path=BaseConfig.W_CHROME_PATH, options=chrome_options)
        elif browser_name == Browsers.IE.value:
            return webdriver.Ie(BaseConfig.W_IE_PATH)
        elif browser_name == Browsers.EDGE.value:
            return webdriver.Edge(BaseConfig.W_EDGE_PATH)
        else:
            error = "No such " + browser_name + " browser exists"
            logger.exception(error)
            raise AutomationError(error)

    @classmethod
    @automation_logger(logger)
    def get_driver_lin(cls, browser_name):
        """
        Choose needed driver according to Linux OS.
        :param browser_name: Chrome, Firefox
        :return: web driver.
        """
        if browser_name == Browsers.FIREFOX.value:
            try:
                return webdriver.Firefox(executable_path=GeckoDriverManager().install())
            except Exception as e:
                logger.exception(e)
                return webdriver.Firefox(executable_path=BaseConfig.L_FIREFOX_PATH)
        elif browser_name == Browsers.CHROME.value:
            try:
                return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=cls.chrome_options)
            except Exception as e:
                logger.exception(e)
                return webdriver.Chrome(executable_path=BaseConfig.L_CHROME_PATH, options=cls.chrome_options)
        else:
            error = "No such " + browser_name + " browser exists"
            logger.exception(error)
            raise AutomationError(error)

    @classmethod
    @automation_logger(logger)
    def get_driver_mac(cls, browser_name):
        """
        Choose needed driver according to Darwin OS.
        :param browser_name: Chrome, Firefox
        :return: web driver for mac.
        """
        if browser_name == Browsers.FIREFOX.value:
            try:
                return webdriver.Firefox(executable_path=GeckoDriverManager().install())
            except Exception as e:
                logger.exception(e)
                return webdriver.Firefox(executable_path=BaseConfig.M_FIREFOX_PATH)
        elif browser_name == Browsers.CHROME.value:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option('w3c', False)
            try:
                return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
            except Exception as e:
                logger.exception(e)
                return webdriver.Chrome(executable_path=BaseConfig.M_CHROME_PATH, options=chrome_options)
        else:
            error = "No such " + browser_name + " browser exists"
            logger.exception(error)
            raise AutomationError(error)

    @classmethod
    @automation_logger(logger)
    def get_webdriver_container(cls, browser_name):
        """
        Provides driver as Docker container..
        :param browser_name: Chrome, Firefox
        :return: web driver.
        """
        if browser_name == Browsers.FIREFOX.value:
            return BrowserWebDriverContainer(DesiredCapabilities.FIREFOX)
        elif browser_name == Browsers.CHROME.value:
            return BrowserWebDriverContainer(DesiredCapabilities.CHROME)
        else:
            error = "No such " + browser_name + " container exists"
            logger.exception(error)
            raise AutomationError(error)

    @classmethod
    @automation_logger(logger)
    def start_selenium_server(cls, browser_name):
        """

        :param browser_name:
        """
        multiprocessing.Process(target=cls.start_server(browser_name)).start()

    @classmethod
    @automation_logger(logger)
    def start_server(cls, browser_name):
        """
        Calls self method run_command_in to start selenium-standalone-server.jar.
        :param browser_name:
        """
        browser_name = browser_name.lower()
        if browser_name == Browsers.FIREFOX.value:
            option = "-Dwebdriver.firefox.driver=" + BaseConfig.W_FIREFOX_PATH
        elif browser_name == Browsers.CHROME.value:
            option = "-Dwebdriver.chrome.driver=" + BaseConfig.W_CHROME_PATH
        elif browser_name == Browsers.IE.value:
            option = "-Dwebdriver.ie.driver=" + BaseConfig.W_IE_PATH
        elif browser_name == Browsers.EDGE.value:
            option = "-Dwebdriver.edge.driver=" + BaseConfig.W_EDGE_PATH
        else:
            error = "No such " + browser_name + " browser exists"
            logger.exception(error)
            raise AutomationError(error)

        command = ["java", option, "-jar", BaseConfig.SELENIUM_JAR]
        cls.run_terminal_command(command)

    @staticmethod
    @automation_logger(logger)
    def run_terminal_command(command):
        """

        :param command:
        """
        subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
