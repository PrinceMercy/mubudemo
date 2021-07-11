from apitest.api import BaseApi

def test_version():
    from apitest import __version__
    assert isinstance(__version__,str)

class ApiHttpbinGet(BaseApi):
    url = "http://httpbin.org/get"
    method = "GET"
    params = {}
    headers = {"accept":"application/json"}

    # def set_params(self,**params):
    #     self.params = params
    #     return self

    # def run(self):
    #     self.response = requests.get(self.url,params=self.params,headers=self.headers)
    #     return self

    # def validate(self,key,expected_value):
    #     actual_value = getattr(self.response,key)
    #     assert actual_value == expected_value
    #     return self

# def test_httpbin_get():
#     resp = requests.get(
#         "http://httpbin.org/get",
#         headers={"accept":"application/json"}
#         )
#     assert resp.status_code == 200
#     assert resp.headers['server'] == 'gunicorn/19.9.0'
#     assert resp.json()['url'] == 'http://httpbin.org/get'

def test_httpbin_get():
    ApiHttpbinGet().run()\
        .validate("status_code",200)\
        .validate("headers.server",'gunicorn/19.9.0')\
        .validate("headers.content-type","application/json")\
        .validate("url","http://httpbin.org/get")

# def test_httpbin_get_with_params():
#     resp = requests.get(
#         "http://httpbin.org/get",
#         headers={"accept":"application/json"},
#         params={"abc":123}
#         )
#     assert resp.status_code == 200
#     assert resp.headers['server'] == 'gunicorn/19.9.0'
#     assert resp.json()['url'] == 'http://httpbin.org/get?abc=123'

def test_httpbin_get_with_params():
    params = {"abc":123,"xyz":456}
    ApiHttpbinGet()\
        .set_params(abc=123,xyz=456)\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server",'gunicorn/19.9.0')\
        .validate("url","http://httpbin.org/get?abc=123&xyz=456")\
        # .validate("content.abc","123")\
        # .validate("content.args.xyz","456")

class ApiHttpbinPost(BaseApi):
    url = "http://httpbin.org/post"
    method = "POST"
    json = {}
    data= ""
    headers = {"accept":"application/json"}

    # def set_params(self,**params):
    #     self.params = params
    #     return self
    # def set_json(self,json):
    #     self.json = json
    #     return self
    
    # def set_data(self,data):
    #     self.set_data = data
    #     return self

    # def run(self):
    #     self.response = requests.post(self.url,json=self.json,headers=self.headers)
    #     return self

    # def validate(self,key,expected_value):
    #     actual_value = getattr(self.response,key)
    #     assert actual_value == expected_value
    #     return self

# def test_httpbin_post():
#     resp = requests.post(
#         "http://httpbin.org/post",
#         headers={"accept":"application/json"}
#         )
#     assert resp.status_code == 200
#     assert resp.headers['server'] == 'gunicorn/19.9.0'
#     assert resp.json()['url'] == 'http://httpbin.org/post'
 
def test_httpbin_post():
    ApiHttpbinPost()\
        .run()\
        .validate("status_code",200)


# def test_httpbin_post_with_data():
#     resp = requests.post(
#         "http://httpbin.org/post",
#         headers={"accept":"application/json"},
#         data={"abc":123}
#         )
#     assert resp.status_code == 200
#     assert resp.headers['server'] == 'gunicorn/19.9.0'
#     assert resp.json()['url'] == 'http://httpbin.org/post'
#     print(resp.json())
#     assert resp.json()["form"]["abc"] == "123"

def test_httpbin_post_with_data():
    ApiHttpbinPost()\
        .set_json({"abc":123})\
        .run()\
        .validate("status_code",200)