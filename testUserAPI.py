import pytest
import requests
import json
class TestAPI:
    @pytest.fixture
    def url(self):
        url = "https://reqres.in/api/users/22"
        return url
    #Checking that the url response is failed .
    def test_url_N(self ):
        url1 = "https://reqredsfsfsfsfss.in/api/users"
        response = requests.get(url1)
        assert 400> response.status_code>=200
    #Checking that user number 22 is empty .
    def test_user22(self, url):
           response = requests.get(url)
           user22 = response.json()
           expected={}
           assert user22 ==expected