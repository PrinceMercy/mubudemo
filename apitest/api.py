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
        value = self.response
        for _key in key.split("."):
            print("value---",_key,value,type(value))
            if isinstance(value,requests.Response): 
                value = getattr(self.response,_key)
            elif isinstance(value,requests.structures.CaseInsensitiveDict):
                value = value[_key]
            # elif isinstance(value,bytes):
            #     value = value[_key]
            # print("value---",value,type(value))
        # actual_value = getattr(self.response,key)
        assert value == expected_value
        return self