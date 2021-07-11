import requests

class BaseApi(object):
    method = ""
    params = {}
    headers = {}
    json={}
    data=""

    def set_params(self,**params):
        self.params = params
        return self

    def set_json(self,json):
        self.json = json
        return self
    
    def set_data(self,data):
        self.set_data = data
        return self
    
    def run(self):
        self.response = requests.request(self.method,
                                    self.url,
                                    params=self.params,
                                    json=self.json,
                                    data = self.data,
                                    headers=self.headers
                                    )
        return self

    def validate(self,key,expected_value):
        actual_value = getattr(self.response,key)
        assert actual_value == expected_value
        return self