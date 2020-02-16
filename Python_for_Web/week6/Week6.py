################ JAVASCRIPT OBJECT NOTATION ################

# JSON represents data as nested "lists" and "dictionaries"

# json1.py example

import json
data = '''{
    "name": "Chuck",
    "phone" : {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"}
}'''

info = json.loads(data) ## <- deserialize step 

# what you get back is a native dictionary

print 'Name:' , info["name"]
print 'Hide:' , info["email"]["hide"]

# json2.py example

import json

input = '''
[    
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  } 
]'''

info = json.loads(input)
print 'User count:', len(info)

for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']


############# SERVICE ORIENTED APPROACH ################

# Most non-trivial web applications use services

# They use services from other applications
# - Credit card charge
# - Hotel reservation systems

# Services publish the "rules" applications must follow to make use of the service (API)

# MULTIPLE SYSTEMS

# Initially - two systems cooperate and splite the problem

# As the data/service becomes useful - multiple applications want to use the information/application


################ ACCESSING APIS IN PYTHON ################

# Aplication Program Interface: The API itself is largely abstract in that it specifies an interface and controls the behavior of the objects specified in that interface.  The software that provides the functionality described by an API is said to be an "implementation" of the API. An API is typically defined in terms of the programming language used to build an application.  

# Web Service Technologies

# SOAP - Simple Object Access Protocol (software)
# - Remote programs/code which we use over the network
# REST - Representational State Transfer (resource focused)
# - Remote resources which we create, read, update and delete remotely

# Google Geocoding API

# geojson.py example

import urllib
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
    
    
# API Security and Rate Limiting
## The compute resources to run these APIs are not "free"
## The data provided by these APIs is usually valuable
## The data providers might limit the number of requests per day, demand an API "key", or even charge for usage
## They might change the rules as things progress...

################ API SECURITY AND RATE LIMITING ################

# Using the Twitter API

# Service oriented architecture - allows an application to be broken into parts and distributed across a network

# An API is a contract for interaction

# Web Services provide infrastructure for applications cooperating (an API) over a network - SOAP and REST are two styles of web services 

# XML and JSON are serialization formats


