
CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Technologies
 * Requirements
 * Tests
 * Configuration
 * Python Installation
 * Maintainers

INTRODUCTION
------------

This is a final task provided as part of interview (third day) of "Taranis" company.
Automation test framework covers backend and frontend, provides functionality for testing:

- API
- UI
- EndToEnd


TECHNOLOGIES
-------------

- pytest - advanced test framework.
- allure-pytest - reporting.
- selenium - test framework.
- requests - HTTP/S requests.


REQUIREMENTS
------------

1. PyCharm IDEA installed.
2. Python 3.6 or later installed.
3. Python virtualenvironment installed and activated.
4. Python interpreter configured.
5. Project requirements installed.
6. Project plugins installed.

TESTS
-----

1 Run all tests:
* $ pytest -v . --alluredir=allure_results

2 Run tests as a package:
* $ pytest -v ui_tests --alluredir=allure_results

3 Run specific test:
* $ pytest -v ui_tests/main_page_tests.py  --alluredir=allure_results

4 Run per test group (public_api group as example):
* $ pytest -v . -m ui --alluredir=allure_results

5 Generate allure report:
* Go to scripts and run: allure_results.sh
* Go to scripts and run: allure_reports.sh

* Test Groups:

1. ui - ui tests except smoke
2. e2e - end to end tests
3. api - api tests


CONFIGURATION
--------------

- Project base configuration stores in config.cfg that processes by config_definitions.py class.

- All imports specified in the requirements.txt file.

* To install all project dependencies run command:
* $ pip install -r requirements.txt


Python Installation:  
--------------------
https://www.python.org/downloads/

* install pip:
$ python get-pip.py

* install virtual environment:
$ pip install virtualenv

* create virtual environment:
$ virtualenv venv --python=python3.7

* activate environment for Windows:
$ venv\Scripts\activate

* activate environment for Unix:
$ source venv/bin/activate

* list all packages installed in the environment:
$ pip freeze

* upgrade pip:  
$ python -m pip install --upgrade pip


MAINTAINERS
-----------

* Anton Shipulin <antishipul@gmail.com> 
