import requests
import pytest 
import yaml 


#url,arguments={},headers={},cookies={},data={},predictions={}




def pytest_generate_tests(metafunc):
    with open('data.yaml', 'r') as f:
        doc = yaml.load(f)


    arr = []
    with open('data.yaml', 'r') as f:
        doc = yaml.load(f)

    for key in doc["tests"] : 
        url = doc["tests"]["test1"]["url"]
        headers = doc["tests"]["test1"]["headers"]
        data = doc["tests"]["test1"]["data"]
        arr.append((url,headers,data))  
     
    metafunc.parametrize( ("url","headers","data") , arr) 

def test_func(url , headers, data):
    print "\n inside test func"
    print url 
    print headers 
    print url 
    assert 200 == 200 






#############






def test_post_request():
    with open('data.yaml', 'r') as f:
        doc = yaml.load(f)

    print  doc["tests"].keys()
    arr = []

    for key in doc["tests"] : 
        url = doc["tests"]["test1"]["url"]
        headers = doc["tests"]["test1"]["headers"]
        data = doc["tests"]["test1"]["data"]
        arr.append((url,headers,data))  
        
        print "i am here" + key 
        response = requests.post(
            url, 
            data=data,
            headers=headers 
        )

        print response
        assert response.status_code == 200
        #assert response.text == "foo" 
        #assert response.json()["price"] == 5.5 

    print arr




#test_post_request()
#url,"foo",headers,"cook",data) 

