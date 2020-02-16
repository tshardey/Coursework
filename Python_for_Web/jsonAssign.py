import json
import urllib

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break
    
    print 'Retrieving', url
    input = urllib.urlopen(url)
    data = input.read()
    print 'Retrieved',len(data),'characters'

    info = json.loads(str(data))
    
    print json.dumps(info, indent=4)
    
    totalCount = list()
    
    for item in info["comments"]:
        count = int(item['count'])
        totalCount.append(count)
        
    print 'User count:', len(totalCount)    
    print 'Sum:', sum(totalCount)     