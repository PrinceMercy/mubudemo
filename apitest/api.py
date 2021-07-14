import requests
from requests import sessions

#session的共用，session的请求和request的请求是一样的
session = requests.sessions.Session()

class BaseApi(object):
    method = ""
    url=''
    params = {}
    headers = {}
    json={}
    data=""
    cookie = {}

    # def __init__(self) -> None:
    #     self.response = None

    def set_params(self,**params):
        self.params = params
        return self

    def set_json(self,json):
        self.json = json
        return self
    
    def set_data(self,data):
        self.data = data
        return self
    
    def set_cookies(self,key,value):
        self.cookie.update({key:value})
        return self
    
    def run(self):
        self.response = session.request(self.method,
                                    self.url,
                                    params = self.params,
                                    json = self.json,
                                    data = self.data,
                                    cookies = self.cookie,
                                    headers = self.headers
                                    )
        return self
    
    ###约定在validate校验完成功后，再去提取参数值
    def extract(self,field:str):
        value = self.response
        for _key in field.split("."):
            print("ex_value---",_key,value,type(value))
            if isinstance(value,requests.Response):
                if _key == "content":
                    value = self.response.json()
                else:
                    value = getattr(self.response,_key)
            elif isinstance(value,(requests.structures.CaseInsensitiveDict,dict)):
                value = value[_key]
            print("ex_value---22",_key,value,type(value))
        return value

    def validate(self,key:str,expected_value):
        # value = self.response
        # for _key in key.split("."):
        #     # print("value---",_key,value,type(value))
        #     if isinstance(value,requests.Response):
        #         if _key == "content":
        #             value = self.response.json()
        #         else:
        #             value = getattr(self.response,_key)
        #     elif isinstance(value,(requests.structures.CaseInsensitiveDict,dict)):
        #         value = value[_key]
            # elif isinstance(value,bytes):
            #     value = value[_key]
            # print("value---2",value,type(value),expected_value,type(expected_value))
        # actual_value = getattr(self.response,key)
        actual_value = self.extract(key)
        assert actual_value == expected_value
        return self
    
    def get_response(self):
        return self.response