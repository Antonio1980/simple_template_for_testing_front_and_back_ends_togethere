import allure
import pytest
from base.logger import automation_logger, logger

test_case = "TestStaticResources"


@allure.testcase(test_case)
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("api_client")
@allure.description("""
    UI Test.
    1. Check that manifest.json exists and returned status code 200 OK.
    2. Check content of the manifest.json.
    """)
@pytest.mark.api
class TestStaticResources(object):

    @automation_logger(logger)
    def test_manifest_json(self, api_client):
        allure.step("Verify that status code is 200 OK.")
        _response = api_client.get_manifest()
        assert _response[0] is not None
        assert _response[1].status_code == 200
        assert _response[1].reason == "OK"

        logger.info(F"============ TEST CASE {test_case} / 1 PASSED ===========")

    @automation_logger(logger)
    def test_manifest_content(self, api_client):
        allure.step("Verify content of the manifest.json.")
        _response = api_client.get_manifest()[0]
        assert _response is not None
        assert isinstance(_response, dict)
        assert "short_name" and "name" and "icons" and "start_url" and "display" and "theme_color" and \
               "background_color" in _response.keys()
        assert isinstance(_response["icons"], list)
        assert len(_response["icons"]) > 0
        assert isinstance(_response["icons"][0], dict)
        assert "src" and "sizes" and "type" in _response["icons"][0].keys()

        logger.info(F"============ TEST CASE {test_case} / 2 PASSED ===========")

