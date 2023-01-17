import requests
import json
from faker import Faker


class Utilities:
    def __init__(self, shared_object):
        self.SITE_URL = shared_object['SITE_URL']
        self.API_KEY = shared_object['API_KEY']
        self.faker = Faker()

    def send_get_request(self, endpoint, data=None):
        if data is None:
            return requests.get(url=self.SITE_URL + endpoint)
        else:
            return requests.get(url=self.SITE_URL + endpoint, data=data)

    def check_json_is_equals_to_dictionary(self, dictionary, json_data):
        json_data = json.dumps(json_data)
        assert json.loads(json_data) == dictionary
