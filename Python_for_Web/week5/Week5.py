## Week 5 
## Chapter 13

############# WEB SERVICES OVERVIEW ##############

# With the HTTP Request/Response well understood and well supported, there was a natural move toward exchanging data between programs using these protocols.

# We needed to come  up with an agreed way to represent data going between applications and across networks.

# There are two commonly used formats: XML and JSON

# WIRE PROTOCOL - What we send on the "wire" 
## "Wire format" - serialize ---> de-serialize
## ex. XML and JSON

############# eXtensible Markup Language - XML ##############

# Primary purpose is to help information systems share structured data

# It started as a simplified subset of the Standard Generalized Markup Language (SGML), and is designed to be relatively human-legible

# Has advantage when doing documents, but is a little harder

# A textual representation of a tree structure and a node
## greater than and less thans
## A simple element is a tag with text
## A complex element is a tag with tags in it
## <> start tag </> end tag
### Start tag has attributes
### Self closing tag < tag all-info />
## White space tends not to matter, except in textual area
### Used for readability

# Tags - indicate the beginning and ending of elements
# Attributes - Keyword/value pairs on the opening tag of XML
# Serialize/De-serialize - Convert data in one program into common format that can be stored and/or transmitted between systems in a programming language-independent manner

############# XML Schema ##############

# Description of the legal format of an XML document

# Expressed in terms of constraints on the structure and content of documents

# Often used to specify a "contract" between systems - "My system will only accept XML that conforms to this particular Schema."

# If a particular piece of XML meets the specifications of the Schema - it is said to "validate"

# XSD XML Schema (W3C) 

# W3C - World Wide Web Consortium

# file names end in .xsd

# Structure
## xs:complexType
## xs:sequence
## xs:element
## Date format Year-Mo-DaTHr:Mn:ScZ <- UTC Timezone (ISO-8601)

############# Parsing XML in Python ##############

# XML is built into Python
print "Example XML1"

import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')

print "Example XML2"
import xml.etree.ElementTree as ET2

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''

stuff = ET2.fromstring(input)
lst = stuff.findall('users/user')
print 'User count:', len(lst)

for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get("x")








