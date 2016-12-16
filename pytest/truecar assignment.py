


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






def compare (ds, actual  = {}, stack = [] , comparisonFlag = True, errorMessage=None):
    print "function called " 
    print "\t Comparison Flag ---------> " + str (comparisonFlag)
    print  "\t ds value  ", ds
    print  "\t actual value  ", actual 
    print  "\t stack value  ", stack 


    # check if comparison already failed, no need to traverse to rest of the json
    if ( comparisonFlag == False):
        return comparisonFlag, errorMessage


    if type(ds) == dict:

        for key in ds.keys():
            stack.append(key)
            print "\n\tPushing " + key + " to stack . Stack value  " + str ( stack )



            if ( type(ds[key])  == str  or  type(ds[key])  == int ) : 
                print "\t key is a int or string , no need to call func " 
                print "\t ds[key] ", key 
          
                # compare values  ,construct key from stack and get both values 

                actualValue = reduce(lambda d, k: d[k], stack, actual )
                print  "\t Value from actual ", actualValue

                if str (ds[key]) != str(actualValue) :
                    print "\t comparison mismatch between %s and %s" % (  str (ds[key]) ,  str(actualValue) )
                    print "\n\tPushing " + key + " to stack . Stack value  " + str ( stack )
   
                    print "\n\tFailure : For key " + str ( stack ) , 
                    print " The value %s and %s mismatch " % (  str (ds[key]) ,  str(actualValue) )

                    return False,"Values Mismatch "
                else :
                    print "\n\t pop the stack "
                    stack.pop()

                    print "\n\tPopping " + key + " to stack . Stack value  " + str ( stack )
            else : 
                print "\n\tCalling function with ds ", ds[key]
    
                comparisonFlag,errorMessage = compare(ds[key],actual,stack, comparisonFlag, errorMessage)
    
                # check if comparison already failed, no need to traverse to rest of the json
                if ( comparisonFlag == False):
                    return comparisonFlag, errorMessage
    
    
                print "Popping -- " + key
                stack.pop()
                print "\t\t" + str ( stack )
    
        

            '''

            if ds[key] is a string on an int then compare and return flga and errorMsg 

    elif ( type(ds) == str  or  type(ds) == int ) :
        print "Visiting element --> "  + str ( ds )
        print "\t\t" + str ( stack  )


            # if mismatch then set comparisonFlag and return
            if str (ds) != str(actualValue) :
                print "\t comparison mismatch between %s and %s" % (  str (ds) ,  str(actualValue) )
                comparisonFlag = False
                errorMessage = "\tFor %s key, Value mismatch, Expected : %s, Actual : %s" % ( stack, str (ds),  str(actualValue) )
             '''
   


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


    return comparisonFlag, errorMessage
    


actual = {}
expected = {}


actual = {'a': 1,'b' : 2 ,'c' : 3 ,'d' : {'e' : 4 }} 

expected = {'a': 1 , 'c' : 3 , 'd' : {'e' : 41 } } 

# Fail: 
#actual = {'a': 1,'b' : 2 ,'c' : 3 ,'d' : {'e' : 4 }} 
#expected = []


#compare ( actual, expected ) 
compare (  expected, actual  ) 

''' 
# exact ds 
# var missing in act / var missing in exp 
# nested dictinary - happy path / non matching 
# nested dictionarty - nested key missing in actual / exp 

# dictionary 
  # key present and exact 
  # key present and mismatch 
  # key missing in either 
  # null key

# dictionary / nested dictionary 
  # key present and exact 
  # key present and mismatch 
  # key missing in either 
  # null key 
  # Entire nested dictionary or List missing or exact 
  
# dictionary / nested listed 
  # List present and exact 
  # key present and mismatch 
    -> different number of elements 
    -> different elements 
    -> different order of elements 
    -> null array 

# top level
  # null and null 
  # null and proper  for both combinations
    -> against dict 
    -> against list  
    -> against string/int

  # mismatched datatypes 
    -> list and dict 
    -> list and string/int 
    -> dict and string/int 

  # Multiple failures at different level
  # Multiple failures at same level 







# List  / nested List  
  # key present and exact 
  # key present and mismatch 
  # key missing in either 
  # Entire nested dictionary or List missing or exact 

'''







