import requests
import pytest 
import yaml 
import json 

#url,arguments={},headers={},cookies={},data={},predictions={}


def foo():
    print "foo"

def pytest_generate_tests(metafunc):
    
    foo()
    arr = []
    with open('data.yaml', 'r') as f:
        doc = yaml.load(f)
    
    for key in doc["tests"] : 
        url = doc["tests"][key]["url"]
        headers = doc["tests"][key]["headers"]
        cookies = doc["tests"][key]["cookies"] 
        data = json.dumps(doc["tests"][key]["data"])
        arr.append((url,headers,cookies,data))  

    metafunc.parametrize( ("url","headers","cookies","data") , arr) 

def test_func(url , headers, cookies, data):
    print "\n inside test func"
    print data 
    response = requests.post(
            url, 
            data=data,
            headers=headers 
        )

    print response
    print response.text
    assert response.status_code == 200
    assert 200 == 200 
 


