import sys
import json
import re

scores = {} 
newScores = {} 
instances = {} 

# Creates a function that makes a dictionary for the content of the sentiment scores file

def wordDict():
    dictFile = open(sys.argv[1])
    for line in dictFile: # iterates through each tuple in the file
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	  	scores[term] = int(score)  # Convert the score to an integer.

def scoreTweets():
    tweetCount = 1
    tweetFile = open(sys.argv[2])
    for line in tweetFile:
        tweetScore = 0
        result = json.loads(line)
        string = result.get('text','zz').encode('ascii', "ignore")
        words = string.strip().split()
        newWords = []
        for word in words:
        	word = word.encode('utf-8')
        	wordScore = int(scores.get(word, -1000))
        	# Means word was not found in original dictionary
        	if wordScore == -1000:
        		newWords.append(word)
        	else:
        		tweetScore = tweetScore + wordScore
        		# Now check for all new words encountered
        for word in newWords:
            newScores[word]= newScores.get(word,0)+tweetScore
        tweetCount= tweetCount +1
        
def displayWords():
	for key, value in sorted(newScores.iteritems(), key=lambda (k,v): (v,k)):
		print "%s %s" % (key, value)
    
def main():
    wordDict()
    scoreTweets()
    displayWords()

if __name__ == '__main__':
    main()
