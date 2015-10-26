import requests
import pytest 
import yaml 
import json 
import memcache 
#url,arguments={},headers={},cookies={},data={},predictions={}


def foo():
    print "foo"
#
def pytest_addoption(parser):
    parser.addoption("--stringinput", action="append", default=[], help="list of stringinputs to pass to test functions")
    parser.addoption('--foo', action='store_true', help='Do foo')
    parser.addoption('--bar', action='store_false', help='Do not do bar')

def pytest_generate_tests(metafunc):
    
    ######
    #if 'stringinput' in metafunc.fixturenames:
    #    print "string input name " , metafunc.config.option.stringinput

    foo()
    testcase_combinatinos_array = []
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
            testcase_data_dict =  dict ( testdict["default_template"]["data"], **testdict["tests"][key]["data"] )  
            print "INFO : data present for particular test", key 
            print "INFO : data dict ", testcase_data_dict 
            testcase_data_json = json.dumps(testcase_data_dict ) 
        else:
            testcase_data_dict = testdict["default_template"]["data"]

        if "userKV" in testdict["tests"][key]:
            testcase_userKV = testdict["tests"][key]["userKV"]

        # for pretty printing 
        #testcase_data_json = json.dumps(testdict["default_template"]["data"],indent=2) 

        testcase_predictions = dict(testdict["tests"][key]["predictions"])

        testcase_combinatinos_array.append((testcase_url,testcase_headers,testcase_cookies,testcase_data_json ,testcase_predictions,testcase_userKV  ))  

    # parametrize test combinations 
    metafunc.parametrize( ("url","headers","cookies","data","predictions","userKV") , testcase_combinatinos_array) 

    
#    print "merged dict " , dict(default_template_dict, **user_dict) 
#     
#    merged_data_json  =  json.dumps(default_template_dict,indent=2)  
#    print "merged json " , merged_data_json 





def findDiff(d1, d2, path=""):
    print "======= top level keys for d1 " , d1.keys()  
    print "======= top level keys for d2 " , d2.keys()  
    for k in d1.keys():
        print " top level checking for key ", k 
        
        if not d2.has_key(k):
            print path, ":"
            print k + " as key not in d2", "\n"
        else:
            if type(d1[k]) is dict:
                if path == "":
                    path = k
                else:
                    path = path + "->" + k
                findDiff(d1[k],d2[k], path)
            else:
                if d1[k] != d2[k]:
                    print path, ":"
                    print " - ", k," : ", d1[k]
                    print " + ", k," : ", d2[k] 





def validate_prediction(response,predictions):
    assert response.status_code == 200,  "value was odd, should be even"
    assert 200 == 200
    
    response_dict = {} 
    response_dict['headers'] = response.headers
    response_dict['status_code']  = response.status_code
    response_dict['text']    = json.loads(response.text)
     

    print response.text
    #print dict(response.text) 
    print "predictions------->   ", predictions
    print "response_dict -------> " , response_dict
    
    findDiff(predictions,response_dict) 
    #findDiff(response_dict,predictions) 

    #if predictions.viewitems() < response_dict.viewitems() : 
    #if ( predictions.viewitems().issubset(response_dict.viewitems()) ): 
    # Currently compares only keys and NOT values 
    if ( set(predictions).issubset(response_dict) ): 
        assert True ,  "subset " 
    else: 
        assert False , " not subset " 




def test_func(url , headers, cookies, data,predictions,userKV):
    #print "\n inside test func"
    #print data 
    # set KV for userID 
 

    # TODO : implement , one invocation only, Reuse connection 
    mc = memcache.Client(['192.168.150.110:11211'], debug=0)
    print userKV
    
    for key in userKV :
        print key
        mc.set(key, userKV[key])   # note that the key used for incr/decr must be a string.
    # {'network_id.buyerkey_1001': 20.98}




    response = requests.post(
            url, 
            data=data,
            headers=headers 
        )

    #print response
    #print response.text
    #assert response.status_code == 200
    #assert 200 == 200 
    #print  keys(response.cookies)
    validate_prediction(response,predictions)

#         buyerUserID :
#                 network_id.buyerkey_1001 : 20.98


# easier way to generate testcase_combinatinos_array 
# @pytest.mark.parametrize('testdata', [i for i in Iterations])  
# @pytest.mark.parametrize('testdata', [FUNCTUION TO POPULATE AND RETURN testcase_combinatinos_array ]
