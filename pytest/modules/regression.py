import requests
import pytest 
import json 
import memcache
import yaml 
import ast
import demjson


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



def compare (ds, actual  = {}, stack = [] , comparisonFlag = True, errorMessage=None): 
      
    print "\n at start flag ---------> " + str (comparisonFlag) 

    # check if comparison already failed, no need to traverse to rest of the json 
    if ( comparisonFlag == False):
        return comparisonFlag, errorMessage
    

    if type(ds) == dict:
    
        for key in ds.keys():
            stack.append(key) 
            print "Pushing -- " + key 
            print "\t\t" + str ( stack ) 
            comparisonFlag,errorMessage = compare(ds[key],actual,stack, comparisonFlag, errorMessage)

            # check if comparison already failed, no need to traverse to rest of the json 
            if ( comparisonFlag == False):
                return comparisonFlag, errorMessage
 

            print "Popping -- " + key 
            stack.pop()
            print "\t\t" + str ( stack ) 

    elif type(ds) == list:
         i = 0 
         print "in the list"
        # iterate through each item of the list
         for index, item in enumerate(ds):
           
             print index, item
             stack.append(index)
             print "Pushing -- " + str(index)
             print "\t\t" + str ( stack )
             # Start recursive call for item 
             comparisonFlag,errorMessage = compare(ds[index],actual,stack, comparisonFlag, errorMessage) 

             # check if comparison already failed, no need to traverse to rest of the json 
             if ( comparisonFlag == False):
                 return comparisonFlag, errorMessage
 
             print "Popping -- " + str(index )
             stack.pop()
             print "\t\t" + str ( stack )

    elif ( type(ds) == str  or  type(ds) == int ) :
        print "Visiting element --> "  + str ( ds )  
        print "\t\t" + str ( stack  )     
           

 
        # check if the key structure exists for actual 
        try:
            actualValue = reduce(lambda d, k: d[k], stack, actual ) 

        # if no then return False with message 
        except Exception :
            print "exception found"
            comparisonFlag = False 
            errorMessage = "%s Key not present in actual" % (stack) 
            return comparisonFlag , errorMessage

        # if yes , then check if value are same 
        else:
            print "value in expected %s and value in %s " % ( str (ds) ,  str(actualValue) )  
        
            # if mismatch then set comparisonFlag and return              
            if str (ds) != str(actualValue) :
                print "\t comparison mismatch between %s and %s" % (  str (ds) ,  str(actualValue) ) 
                comparisonFlag = False 
                errorMessage = "\tFor %s key, Value mismatch, Expected : %s, Actual : %s" % ( stack, str (ds),  str(actualValue) )
   
        print "\n at condition flag ---------> " + str( comparisonFlag )   

    print "\n at end flag ---------> %s , %s " %  ( str( comparisonFlag ) , str ( errorMessage ) )  
    return comparisonFlag , errorMessage





def verify ( response , predictions ):

    if "status_code" in predictions:
        print "prediction status code %s  and response status code %s " % ( str ( predictions['status_code'] ) , str ( response.status_code ))   
        assert predictions['status_code'] ==  response.status_code	

    if "text" in predictions:
        #assert False  
        print "within verify - response "
        print  ast.literal_eval(response.text)
        print  type(ast.literal_eval(response.text))

        print "within verify - prediction  "
        print predictions['text']
        print type(predictions['text'])
       
        # confirm if text repsone meets prediction 
        comparisonFlag , errorMessage = compare( predictions['text'], ast.literal_eval(response.text) )
        assert comparisonFlag , errorMessage 
        #assert (compare( predictions['text'], ast.literal_eval(response.text) ) )  
        
           


 











