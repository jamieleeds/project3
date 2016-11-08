# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

from textblob import TextBlob

import tweepy

search_term = "Election"

# Unique code from Twitter
access_token = "167086627-yiwlT0HMMj8lH2LVqY3A5vQKNjaIaoCK8Ev0rRi0"
access_token_secret = "gdFYPNFrNAcok13CNYfbuNcFyKaDnQVMNo0lHheYYfPJF"
consumer_key = "BJJgvuesKMOX0Rik05KwCU2rX"
consumer_secret = "kwiZn4MLFOGxHjn3hSt551r9fwMZBqzYtMPmatFudjQxBEvBrF"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search(search_term)

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment.polarity)
	print(analysis.sentiment.subjectivity)

import statistics 

polarity_list = [TextBlob(tweet.text).sentiment.polarity for tweet in public_tweets]
subjectivity_list = [TextBlob(tweet.text).sentiment.subjectivity for tweet in public_tweets]

polarity_list_average = statistics.mean(polarity_list)
subjectivity_list_average = statistics.mean(subjectivity_list)

print("Average subjectivity is", subjectivity_list_average)
print("Average polarity is", polarity_list_average)
