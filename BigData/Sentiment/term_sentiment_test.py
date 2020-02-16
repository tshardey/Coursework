import sys
import json

# Create a dictionary for the content of the sentiment scores

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

tweets_filename = 'problem_1_submission.txt'
tweets_file = open(tweets_filename, "r")

# Selecting just the text from each of the tweets

tweetContent = list()

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            tweetContent.append(tweet['text']) # content of the tweet

    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue


for row in tweetContent:
    words = row.split()
    for word in words:
        for define, amount in scores.items():
            if word == define.decode('utf-8'):
                print word



            
             

