import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break
    
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)

    lst = tree.findall('comments/comment')
    print 'Count:', len(lst)
    
    numList = list()
    for item in lst:
        strNum = item.find('count').text
        num = float(strNum)
        
        numList.append(num)
        
    print 'Sum:', sum(numList)
        
        
        


