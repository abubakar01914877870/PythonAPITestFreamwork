import pytest
import requests
from util.Utilities import Utilities

class TestGetRequest:

    @pytest.mark.get
    @pytest.mark.sanity
    def test_get_endpoint_status_code(self, shared_variables):
        util = Utilities(shared_variables)
        response = util.send_get_request(endpoint="/get")
        assert response.status_code == 200
        print(response.headers)

    @pytest.mark.get
    def test_get_request_body(self, shared_variables):
        util = Utilities(shared_variables)
        data = {"message": "Test Message"}
        response_json = util.send_get_request(endpoint="/get", data=data).json()
        util.check_json_is_equals_to_dictionary(data, response_json['args'])

    @pytest.mark.get
    def test_check_response_header(self, shared_variables):
        util = Utilities(shared_variables)
        response = util.send_get_request(endpoint="/get")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

        # Negative Test Case: Send a request to the API endpoint with invalid input and
        # verify that the API returns a 400 Bad Request status code and the expected error message.
        @pytest.mark.get
        def test_create_user_with_invalid_data(self, shared_variables):
            util = Utilities(shared_variables)
            response = requests.get(util.SITE_URL + "/basic-auth")
            assert response.status_code == 401
            assert response.text == "Unauthorized"

        # Check basic auth
        @pytest.mark.get
        def test_basic_auth_user_password(self, shared_variables):
            util = Utilities(shared_variables)
            user = "postman"
            password = "password"
            response = requests.get(util.SITE_URL + "/basic-auth", auth=(user, password))
            assert response.status_code == 200
