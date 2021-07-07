
def test_version():
    from apitest import __version__
    assert isinstance(__version__,str)

import requests
def test_httpbin_get():
    resp = requests.get(
        "http://httpbin.org/get",
        headers={"accept":"application/json"}
        )
    assert resp.status_code == 200
    assert resp.headers['server'] == 'gunicorn/19.9.0'
    assert resp.json()['url'] == 'http://httpbin.org/get'

def test_httpbin_get_with_params():
    resp = requests.get(
        "http://httpbin.org/get",
        headers={"accept":"application/json"},
        params={"abc":123}
        )
    assert resp.status_code == 200
    assert resp.headers['server'] == 'gunicorn/19.9.0'
    assert resp.json()['url'] == 'http://httpbin.org/get?abc=123'

def test_httpbin_post():
    resp = requests.post(
        "http://httpbin.org/post",
        headers={"accept":"application/json"}
        )
    assert resp.status_code == 200
    assert resp.headers['server'] == 'gunicorn/19.9.0'
    assert resp.json()['url'] == 'http://httpbin.org/post'

def test_httpbin_post_with_data():
    resp = requests.post(
        "http://httpbin.org/post",
        headers={"accept":"application/json"},
        data={"abc":123}
        )
    assert resp.status_code == 200
    assert resp.headers['server'] == 'gunicorn/19.9.0'
    assert resp.json()['url'] == 'http://httpbin.org/post'
    print(resp.json())
    assert resp.json()["form"]["abc"] == "123"