import requests
import pytest 
import json 
from modules.regression import * 
import modules.regression







def test_1():
    ''' 
    This is a demo test case 
    '''
    request = {
             "data"    : {"publisher_id":11111,"site_id":161,"pmp":{"deals":[{"floor":0.24,"seats":["r1"]}]},"device":{"os":"26000"},"ad_size_id":2,"instl":1},
             "headers" : {'Content-Type':'application/json', 'cookie': 'returnBidAmount=5.2345' },
             "cookies" : {"put_x": 100},
             "params"  : {'sessionKey': '9ebbd0b2', 'format': 'xml', 'platformId': 1}
              }

    populateKeyValue("abc", 1234)   # note that the key used for incr/decr must be a string.
    print "get value from memcache -----> ", getKeyValue("abc") 

    predictions = { "status_code": 200,
                    "text": { "seatbid":  [{ "bid": [{ "price": 5.2345}], "seats": "testseat"}]}
                  }

    response = callFakeBidder ( request ) 
    verify ( response , predictions ) 

    # place for additional assertions  
    assert 1 == 1    

def test_2():
    ''' 
    This is a demo test case 
    '''
    request = {
             "data"    : {"publisher_id":11111,"site_id":161,"pmp":{"deals":[{"floor":0.24,"seats":["r1"]}]},"device":{"os":"26000"},"ad_size_id":2,"instl":1},
             "headers" : {'Content-Type':'application/json', 'cookie': 'returnBidAmount=5.2345' },
             "cookies" : {"put_x": 100},
             "params"  : {'sessionKey': '9ebbd0b2', 'format': 'xml', 'platformId': 1}
              }

    predictions = { "status_code": 200,
                    "text": { "seatbid":  [{ "bid": [{ "price": 5.2345}], "seats": "testseat"}]}
                  }

    response = callFakeBidder ( request ) 
    verify ( response , predictions ) 

    # place for additional assertions  
    assert 0 == 0 

