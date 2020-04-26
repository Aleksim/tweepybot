import tweepy
import time
import dotenv
import sys
import os

dotenv.load_dotenv()

apikey = os.getenv('API_KEY')
apisecretkey = os.getenv('API_SECRET_KEY')
accesstoken = os.getenv('ACCESS_TOKEN')
accesstokensecret = os.getenv('ACCESS_TOKEN_SECRET')

print(apikey)

auth=tweepy.OAuthHandler(apikey, apisecretkey)
auth.set_access_token(accesstoken, accesstokensecret)

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search= 'sãopaulo'
nrTweets= 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('tweet liked')
        tweet.favorite()
        time.sleep(10)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
    
