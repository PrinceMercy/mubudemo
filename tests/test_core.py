# from requests.api import request
from tests.api.httpbin import *

# class ApiHttpbinGet(BaseApi):
#     url = "http://httpbin.org/get"
#     method = "GET"
#     params = {}
#     headers = {"accept":"application/json"}

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
        .validate("content.url","http://httpbin.org/get")

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
        .set_params(a=123,b=231)\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server",'gunicorn/19.9.0')\
        .validate("content.url","http://httpbin.org/get?a=123&b=231")\
        .validate("content.args.a","123")\
        .validate("content.args.b","231")\
        # .validate("content.args",{"abc":123,"xyz":456})

# class ApiHttpbinPost(BaseApi):
#     url = "http://httpbin.org/post"
#     method = "POST"
#     json = {}
#     data= ""
#     headers = {"accept":"application/json"}

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
        .validate("status_code",200)\
        .validate("headers.server",'gunicorn/19.9.0')\
        .validate("content.url","http://httpbin.org/post")


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

def test_httpbin_post_with_json():
    ApiHttpbinPost()\
        .set_json({"abc":123})\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server",'gunicorn/19.9.0')\
        .validate("content.url","http://httpbin.org/post")\
        .validate("content.json.abc",123)\
        .validate("content.data",'{"abc": 123}')

# def test_httpbin_post_with_data():
#     ApiHttpbinPost()\
#         .set_data([1,2])\
#         .run()\
#         .validate("status_code",200)\
#         .validate("headers.server",'gunicorn/19.9.0')\
#         .validate("content.url","http://httpbin.org/post")\
#         .validate("content.json.abc",123)

def test_httpbin_parameters_share():
    user_id = "aa1123"
    ApiHttpbinGet()\
        .set_params(userid=user_id)\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server",'gunicorn/19.9.0')\
        .validate("content.url","http://httpbin.org/get?userid={}".format(user_id))\
        .validate("content.args.userid","aa1123")
    
    ApiHttpbinPost()\
        .set_json({"userid":user_id})\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server",'gunicorn/19.9.0')\
        .validate("content.url","http://httpbin.org/post")\
        .validate("content.json.userid","aa1123")

def test_httpbin_extract():
    api_run = ApiHttpbinPost()\
        .set_json({"abc":123})\
        .run()

    status_code =api_run\
        .validate("status_code",200)\
        .extract("status_code")
    assert status_code == 200

    server = api_run\
        .validate("status_code",200)\
        .extract("headers.server")
    assert server == 'gunicorn/19.9.0'

    accep_json = api_run\
        .extract("content.json.abc")
    assert accep_json == 123

def test_httpbin_setcookies():
    api_run = ApiHttpbinGetCookies()\
        .set_cookies("freeform","234")\
        .set_cookies("freeform2","334")\
        .run()
    freeform = api_run\
        .validate("status_code",200)\
        .validate("headers.server",'gunicorn/19.9.0')\
        .validate("content.cookies.freeform",'234')\
        .extract("content.cookies.freeform")
    
    freeform2 = api_run\
        .validate("status_code",200)\
        .validate("headers.server",'gunicorn/19.9.0')\
        .validate("content.cookies.freeform2",'334')\
        .extract("content.cookies.freeform2")
    
    assert freeform == '234'
    assert freeform2 == '334'
    # ApiHttpbinGetCookies()\
    #     .run()\
    #     .validate("status_code",200)\
    #     .validate("headers.server",'gunicorn/19.9.0')\
    #     .validate("content.cookies.freeform","{}".format(cookie_data))

def test_httpbin_parameters_extract():
    #step 1: get value
    cookie_data = ApiHttpbinGetCookies()\
        .set_cookies("freeform2","334")\
        .run()\
        .extract("content.cookies.freeform2")
    
    #step 2: use value as parameters
    freeform = ApiHttpbinSetCookies()\
        .set_params(freeform=cookie_data)\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server",'gunicorn/19.9.0')\
        .validate("content.cookies.freeform","{}".format(cookie_data))\
        .extract("content.cookies.freeform")
    
    assert freeform == str(cookie_data)

def test_httpbin_login_status():
    #step 1:login and get cookie
    ApiHttpbinSetCookies()\
        .set_params(freeform="334")\
        .run()
    
    #step 2:request another api,check cookie
    resp = ApiHttpbinPost()\
        .set_json({"abc":123})\
        .run()\
        .get_response()
    request_header = resp.request.headers
    # print("request_headers=====",request_header)
    assert "freeform=334" in request_header["Cookie"]