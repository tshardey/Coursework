# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

# Asks user for starter URL
url = raw_input('Enter URL - ')
# Asks user for the amount of times they want the link followed
count = raw_input('Enter count: ')
# Asks user for the position of the link on the page
post = raw_input('Enter position: ')

# Initializes a variable to store the amount of time the process is executed
runCount = 0

# Checks to see if the current count is equal to the user defined count, if not code executes
while runCount <= int(count):
    # Prints current URL 
    print "Retreiving:", url
    # Initializes the URL to the current URL
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
    # Initializes a variable to store the current tag position on the page
    runPost = 0
    # Finds each of the tags
    for tag in tags:
        #Checks to see if the tag correspond to the desired position
        if runPost == int(post)-1:
            # Assigns desired url
            url = tag.get('href', None)
            break
        else:
            # If the tag does not match it will increment by one and continue to the next tag
            runPost += 1 
    # Increments the count
    runCount += 1

    
        
        
