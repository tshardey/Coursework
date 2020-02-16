#   unit 04.01

import socket
# library and methond within the library
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Establish the connection between the socket and the address
mysock.connect( ('www.py4inf.com', 80) )
 
 
#  unit 4.02
 
# Most common protocol is HTTP (Hypertext Transport Protocol)
## The set of rules that tells browsers what they need to do when talking to servers
# URL (Uniform resource locator)

#   unit 4.03

mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if (len(data) <1):
        break
    print data
mysock.close()

# urllib

import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
    print line.strip()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print counts
    