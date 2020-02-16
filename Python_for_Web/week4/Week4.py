## Understanding HTML

# Web Scraping - When a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts information, and then looks at more web pages.
# Search engines scrape web pages - we call this "spidering the web" or "web crawling"

# Why scrape?
## Pull data - particularly social data
## Get your own data back out of some system that has no "export capability"
## Monitor a site for new information
## Spider the web to make a database for a search engine

##  BEAUTIFUL SOUP

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a')

for tag in tags:
    print tag.get('href', None)
    
# SUMMARY

## The TCP/IP gives us pipes/sockets between applications
## WE designed application protocols to make use of these pipes
## HyperText Transport Protocol (HTTP) is a simple yet powerful protocol
## Python has good support for sockets, HTTP,...