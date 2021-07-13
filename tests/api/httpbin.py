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