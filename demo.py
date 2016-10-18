import tweepy
from textblob import TextBlob
import csv
import codecs

threshold = 0.3

# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


'''reference: 
1. http://www.markhneedham.com/blog/2015/05/21/python-unicodeencodeerror-ascii-codec-cant-encode-character-uxfc-in-position-11-ordinal-not-in-range128/
2. http://textblob.readthedocs.io/en/dev/api_reference.html
3. https://docs.python.org/2/library/csv.html
4. Limitation: The tweet text itself might have ',' which can be a problem for csv reader.
'''

with open('sentiment_polarity.csv', 'w') as csvfile:
	polaritywriter = csv.writer(csvfile, delimiter=',',quotechar='\"', quoting=csv.QUOTE_ALL)
        polaritywriter.writerow( ('Tweet', 'Sentiment') )
	for tweet in public_tweets:
	    print(tweet.text)
	     
	    #print(tweet.text.encode("utf-8"))
	    #Step 4 Perform Sentiment Analysis on Tweets
	    analysis = TextBlob(tweet.text)
	    if(threshold<analysis.sentiment[0] and 0.5<analysis.sentiment[1]):
		    polaritywriter.writerow([tweet.text.replace("\"", "'").replace("\n", " ").encode("utf-8"), "Positive"])
	    else:
		    polaritywriter.writerow([tweet.text.replace("\"", "'").replace("\n", " ").encode("utf-8"), "Negative"])	
    
