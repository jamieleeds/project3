# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

import tweepy

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

message = "#UMSI-206 #Proj3"
filename = "University-of-Michigan-800x430.jpg"

api.update_with_media(filename, status=message) 

