import tweepy
from textblob import TextBlob
from kafka import KafkaProducer
import json

with open('config.json') as json_file:
    data = json.load(json_file)

CONSUMER_KEY = data['CONSUMER_KEY']
CONSUMER_SECRET = data['CONSUMER_SECRET']
ACCESS_TOKEN = data['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = data['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda K:json.dumps(K).encode('utf-8'))

# Create API object
api = tweepy.API(auth)

cursorr = tweepy.Cursor(api.search_tweets,q="crypto",tweet_mode='extended').items(100)

for tweet in cursorr:
    producer.send('testTopic',tweet.full_text)