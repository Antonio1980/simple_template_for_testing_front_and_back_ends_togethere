import os
import configparser
from tests_base.drivers import drivers_dir


def get_parser(config):
    parser = configparser.ConfigParser()
    with open(config, mode='r', buffering=-1, closefd=True):
        parser.read(config)
        return parser


class BaseConfig:

    config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg')
    parser = get_parser(config_file)

    BASE_URL = parser.get('BASE_URL', 'base_url')

    UI_DELAY = parser.get('ARGS', 'ui_delay')

    W_CHROME_PATH = drivers_dir + parser.get('WEB_DRIVER_WIN', 'w_chrome')
    W_FIREFOX_PATH = drivers_dir + parser.get('WEB_DRIVER_WIN', 'w_firefox')
    W_IE_PATH = drivers_dir + parser.get('WEB_DRIVER_WIN', 'w_ie')
    W_EDGE_PATH = drivers_dir + parser.get('WEB_DRIVER_WIN', 'w_edge')
    W_JS_PATH = drivers_dir + parser.get('WEB_DRIVER_WIN', 'w_js')

    L_CHROME_PATH = drivers_dir + parser.get('WEB_DRIVER_LIN', 'l_chrome')
    L_FIREFOX_PATH = drivers_dir + parser.get('WEB_DRIVER_LIN', 'l_firefox')

    M_CHROME_PATH = drivers_dir + parser.get('WEB_DRIVER_MAC', 'm_chrome')
    M_FIREFOX_PATH = drivers_dir + parser.get('WEB_DRIVER_MAC', 'm_firefox')

    SELENIUM_JAR = drivers_dir + parser.get('DATA', 'selenium_jar')
