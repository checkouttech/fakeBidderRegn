import requests
import pytest 
import yaml 
import json 

#url,arguments={},headers={},cookies={},data={},predictions={}


def foo():
    print "foo"

def pytest_generate_tests(metafunc):
    
    foo()
    testcase_array = []
    with open('data.yaml', 'r') as f:
        testdict = yaml.load(f)

    for key in testdict["tests"] : 
        if "url" in testdict["tests"][key]:
            testcase_url = testdict["tests"][key]["url"]
        else: 
            testcase_url = testdict["default_template"]["url"]

        if "headers" in testdict["tests"][key]:
            testcase_headers = testdict["tests"][key]["headers"]
        else: 
            testcase_headers = testdict["default_template"]["headers"]

        if "cookies" in testdict["tests"][key]:
            testcase_cookies = testdict["tests"][key]["cookies"]
        else: 
            testcase_cookies = testdict["default_template"]["cookies"]

        if "data" in testdict["tests"][key]:
            # Merge user data on top of default data
            testcase_data_dict =  dict ( testdict["default_template"]["data"], **testdict["tests"]["test3"]["data"] )  
        else:
            testcase_data_dict = testdict["default_template"]["data"]

        testcase_data_json = json.dumps(testdict["default_template"]["data"],indent=2) 

        testcase_array.append((testcase_url,testcase_headers,testcase_cookies,testcase_data_json))  

    metafunc.parametrize( ("url","headers","cookies","data") , testcase_array) 

    
#    print "merged dict " , dict(default_template_dict, **user_dict) 
#     
#    merged_data_json  =  json.dumps(default_template_dict,indent=2)  
#    print "merged json " , merged_data_json 


def test_func(url , headers, cookies, data):
    #print "\n inside test func"
    #print data 
    response = requests.post(
            url, 
            data=data,
            headers=headers 
        )

    #print response
    #print response.text
    assert response.status_code == 200
    assert 200 == 200 
 


