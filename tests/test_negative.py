import pytest
import requests

from util.Utilities import Utilities


class TestNegative:
    @pytest.mark.post
    @pytest.mark.xfail
    def test_expected_fail(self, shared_variables):
        util = Utilities(shared_variables)
        data = {'name': 'Sunny', 'role': 'Admin'}
        response = requests.post(url=util.SITE_URL + "/post", data=data)
        assert response.status_code == 400
