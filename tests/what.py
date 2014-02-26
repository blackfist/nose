import json
from nose.tools import assert_equals
import os
from jsonschema import validate, ValidationError

dataPath = '../data'
schema = json.loads(open('schema.json').read())

def checkOne(inDict,inFileName):
    try:
        validate(inDict,schema)
        pass
    except ValidationError as e:
        offendingPath = '.'.join(str(x) for x in e.path)
        print "Error in %s %s: %s." % (inFileName,offendingPath,e.message)
        assert False

def test_Validity():
    for eachDataFile in os.listdir(dataPath):
        dataToValidate = json.loads(open(os.path.join(dataPath,eachDataFile)).read())
        yield checkOne, dataToValidate, os.path.join(dataPath,eachDataFile)

'''        
        try:
            assert_equals(validate(dataToValidate,schema)
        except ValidationError as e:
            offendingPath = '.'.join(str(x) for x in e.path)
            print "Error in %s %s: %s." % (eachDataFile,offendingPath,e.message)
'''
