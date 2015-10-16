#!/usr/bin/env python

import json
import yaml

#f = open('tree.yaml')
#dataMap = yaml.load(f)
#f.close()

stream = open("data.yaml", 'r')
foo = yaml.load(stream)

print "Length : %d" 
print len(foo) 

print foo 

print  foo["tests"].keys()

print foo["tests"]["test1"]["data"]

d =   json.dumps(foo["tests"]["test1"]["data"]) 

print d


