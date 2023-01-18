import pytest


@pytest.fixture
def shared_variables():
    """
    This fixture hold all of shared variables.
    SITE_URL: Domain url for test site
    API_KEY: API key will go here and shared all test
    """
    SITE_URL = "http://postman-echo.com"
    API_KEY = ""
    shared_variables = {'SITE_URL': SITE_URL, 'API_KEY': API_KEY}
    return shared_variables
    


def pytest_configure(config):
    markers = {"get": "This is the description for marker1",
               "post": "This is the description for marker2",
               "put": "This is the description for marker3",
               "delete": "test ",
               "sanity": "test "
               }
    for marker, description in markers.items():
        config.addinivalue_line("markers", f"{marker}: {description}")

def pytest_html_report_title(report):
    """
    Test Report Title
    """
    report.title = "Simple API Test Report"
