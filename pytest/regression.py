import requests
import pytest 
import json 
import memcache


def prepareRequest(request):
    default_template = {}
    default_template['url'] = "http://192.168.150.110:10001/fakebidder/"
    default_template['data'] =    {"accept_language":"en-us,en;q=0.5","auction_id":"e59cf7f965e5634770bec77b8e234e8447da8992","country":"ca","domain_name":"www.bender-testing.com","ip_address":"137.122.14.11","page_url":"","secure":0,"network_user_id":"bid=3.02^robot_tracking=8498431437585754.94","xff":"209.232.44.21","region":"on","user_id":"9c051f73a0b28f3130fcedf6372f75c90f3a89cc","publisher_id":99999,"site_id":42,"designated_site_url":"www.bender-testing.com","user_agent":"python-requests/2.2.1 CPython/2.7.5 Linux/2.6.18-308.13.1.el5","denied_ad_types":[14001,14004,14006,14007,14008,14009,14010,14011,14012,14013,14020,14021,14022,14002,14003,14005,14014,14015,14016,14017,14018,14019],"render_status":"js","site_size_session_count":1,"user_tz":-400,"page_position":"unknown","expandable":0,"supported_tech":[],"private":0,"preferred_seats":["r1"],"pmp":{"deals":[{"id":"TA-99999-r1","floor":0.20000000298023224,"seats":["r1"],"type":2}]},"device":{"os":"25043","dclass":40,"carrier":"Other"},"ad_size_id":1,"ad_width_px":468,"ad_height_px":60,"alt_ads":[],"instl":0}
    default_template['headers'] = {'Content-Type':'application/json', 'cookie': 'returnBidAmount=8.912346345' }
    default_template['cookies'] = {"put_x": 100}
    default_template['params']  = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}


    if "url" in request:
        request['url'] =  request['url']
    else : 
        request['url'] =  default_template['url']

    if "data" in request:
        # Merge user data on top of default data
        merged_data_dict = dict (default_template['data'] , **request['data'] ) 
        #request['data'] =  json.dumps(merged_data_dict)
        request['data'] = merged_data_dict 
    else : 
        request['data'] =  default_template['data']


    if "params" in request:
        request['params'] =  request['params']
    else : 
        request['params'] =  default_template['params']


    if "cookies" in request:
        request['cookies'] =  request['cookies']
    else :
        request['cookies'] =  default_template['cookies']


    if "headers" in request:
        request['headers'] =  request['headers']
    else :
        request['headers'] =  default_template['headers']

    return request 

 
    

def callFakeBidder (request):
    
    # populate with standard values to make full form request 
    request  = prepareRequest(request) 
    response = requests.post(
             request['url'], 
             params=request['params'],
             headers=request['headers'],
             data=json.dumps(request['data'])
    )
   
    return response 




def verify ( response , predictions ):

    if "status_code" in predictions:
        assert predictions['status_code'] ==  response.status_code	

    if "text" in predictions:
        # TODO : this does not works .... 

        # assert if text block is subset of response.text 
        assert  ( predictions['text'].items() <= json.loads(response.text).items()) 



def populateKeyValue(key,value):
    print "populating key value "
    #mc = memcache.Client(['192.168.150.110:11211'], debug=0)
    # how to reuse the session
    mc.set(key, value)   # note that the key used for incr/decr must be a string.

    #print "get value from memcache -----> ", mc.get(key) 
    # create seession 
    # TODO : implement , one invocation only, Reuse connection 
    #mc = memcache.Client(['192.168.150.110:11211'], debug=0)
    # {'network_id.buyerkey_1001': 20.98}



@pytest.fixture(scope="session") 
def memcacheConnection():
    print "######################################### Creating session ###############################"
    mc = memcache.Client(['192.168.150.110:11211'], debug=0)
    return mc 


