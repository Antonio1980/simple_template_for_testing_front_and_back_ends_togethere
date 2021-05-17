import json
from json import JSONDecodeError

import requests

from config_definitions import BaseConfig
from base.constants import RESPONSE_TEXT
from base.logger import logger, automation_logger


class ApiClient(object):
    api_url = BaseConfig.BASE_URL
    headers = {'Content-Type': "application/json", 'Authorization': None,
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    @automation_logger(logger)
    def get_manifest(self):
        uri = self.api_url + "manifest.json"
        try:
            _response = requests.get(uri, headers=self.headers)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as e:
                logger.error(f"Failed to parse response json: {e}")
                if _response.text is not None:
                    body = _response.text
                else:
                    body = _response.reason
            logger.info(RESPONSE_TEXT.format(body))
            return body, _response
        except Exception as e:
            logger.error(F"{e.__class__.__name__} create_api_token failed with error: {e}")
            raise e