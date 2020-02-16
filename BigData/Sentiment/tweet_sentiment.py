import sys
import json
import re



scores = {} # initialize an empty dictionary

# Creates a function that makes a dictionary for the content of the sentiment scores file
def wordDict(dictFile):
	for line in dictFile: # iterates through each tuple in the file
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	  	scores[term] = int(score)  # Convert the score to an integer.

# Creates a function that reads the streaming tweets JSON and parses out the tweet text using regular expressions

def tweetSent(tweetFile):
    for line in tweetFile:
        finalTweetScore = 0
        result = json.loads(line)
        str = result.get('text','zz').encode('utf-8')
        wordsInTweets = re.compile('\w+').findall(str)
        tweetScore(wordsInTweets)

# Calculates the score of the tweet if the word is found in sentiment dictionary

def tweetScore(word):
    finalTweetScore=0
    for w in word:
        if w in scores.keys():
            sentScore = scores[w]
            finalTweetScore = finalTweetScore + sentScore
        else:
            sentScore = 0
            finalTweetScore = finalTweetScore + sentScore
    print finalTweetScore
            
def main():
    sentFile = open(sys.argv[1])
    tweetedFile = open(sys.argv[2])
    wordDict(sentFile)
    tweetSent(tweetedFile)

if __name__ == '__main__':
    main()             

