import pytest

from util.Utilities import Utilities
import requests


class TestPostRequest:

    @pytest.mark.post
    def test_post_request_status_code(self, shared_variables):
        util = Utilities(shared_variables)
        data = {'name': 'Sunny', 'role': 'Admin'}
        response = requests.post(url=util.SITE_URL + "/post", data=data)
        assert response.status_code == 200

    @pytest.mark.post
    def test_post_request_body_json(self, shared_variables):
        util = Utilities(shared_variables)
        json = {'name': 'Sunny', 'role': 'Admin'}
        response_json = requests.post(url=util.SITE_URL + "/post", json=json).json()
        util.check_json_is_equals_to_dictionary(json, response_json['data'])

    @pytest.mark.post
    def test_post_request_body_data(self, shared_variables):
        util = Utilities(shared_variables)
        data = {'name': 'Sunny', 'role': 'Admin'}
        response_json = requests.post(url=util.SITE_URL + "/post", data=data).json()
        util.check_json_is_equals_to_dictionary(data, response_json['form'])

    @pytest.mark.post
    def test_response_time(self, shared_variables):
        util = Utilities(shared_variables)
        data = {'name': util.faker.name(), 'role': 'Admin'}
        response = requests.post(url=util.SITE_URL + "/post", data=data)
        assert response.elapsed.total_seconds() < 2
        print(util.faker.address())

    # Positive Test Case: Send a request to the API endpoint with valid input and verify that the API returns a 200
    # OK status code and the expected output
    @pytest.mark.post
    def test_create_user(self, shared_variables):
        util = Utilities(shared_variables)
        data = {
            "name": util.faker.name(),
            "email": util.faker.email(),
            "password": util.faker.password()
        }
        response = requests.post(url=util.SITE_URL + '/post', json=data)
        assert response.status_code == 200
        util.check_json_is_equals_to_dictionary(data, response.json()['json'])


