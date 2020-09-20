import tweepy
import time

API_KEY = "your api key"
API_SECRET = "your api secret"
TOKEN = "your access token"
TOKEN_SECRET = "your access token secret"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)

twitter_API = tweepy.API(auth)

def newStatus():
    twitter_API.update_status("This is bot tweeting. Hello to all of you good motherfuckers!")

    while True:
        newStatus()
        time.sleep(3600)