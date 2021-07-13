from apitest.api import BaseApi
class ApiHttpbinGet(BaseApi):
    url = "http://httpbin.org/get"
    method = "GET"
    params = {}
    headers = {"accept":"application/json"}


class ApiHttpbinPost(BaseApi):
    url = "http://httpbin.org/post"
    method = "POST"
    json = {}
    data= ""
    headers = {"accept":"application/json"}

class ApiHttpbinSetCookies(BaseApi):
    url = "http://httpbin.org/cookies/set"
    method = "GET"
    json = {}
    data = ''
    headers = {"accept": "text/plain"}

class ApiHttpbinGetCookies(BaseApi):
    url = "http://httpbin.org/cookies"
    method = "GET"
    json = {}
    data = ''
    headers = {"accept": "application/json"}