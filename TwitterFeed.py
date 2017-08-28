from textblob import TextBlob
import tweepy

auth = tweepy.OAuthHandler(consumer_Key, consumer_secret)
auth.set_access_token(access_Token, access_token_secret)
api = tweepy.API(auth)

query='bitcoin OR crypto'
user_tweets = api.search(q=query)

for tweet in user_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
