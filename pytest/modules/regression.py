import requests
import pytest 
import json 
import memcache
import yaml 

class Car(object):
    condition = 'New'
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color

    def drive(self):
        self.condition = 'Used'



def getMemcacheConnection():
    print "######################################### Creating session ###############################"
    mc = memcache.Client(['192.168.150.110:11211'], debug=0)
    return mc 



def getDefaultTemplate():
    # get from yaml 
    print "######################################### Reading template once ##########################"
    with open('conf/data.yaml', 'r') as f:
        default_template = yaml.load(f)['default_template']
 
    return default_template


def setup_module(module):
    global mc 
    mc = getMemcacheConnection()

    print "this is the begining of times " 

    global default_template
    default_template = getDefaultTemplate()
    



def populateKeyValue(key,value):
    print "populating key value "
    #mc = memcache.Client(['192.168.150.110:11211'], debug=0)
    # how to reuse the session
    global mc 
    mc.set(key, value)   # note that the key used for incr/decr must be a string.


def getKeyValue(key): 
    global mc 
    return mc.get(key) 



def prepareRequest(request):
    #default_template = {}

    #print foo['f1']
    global default_template
    # get from yaml 
    with open('conf/data.yaml', 'r') as f:
        default_template = yaml.load(f)['default_template']


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


###############################################################################################################################






