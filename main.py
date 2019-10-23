import tweepy
import json
import re
import webbrowser

# load Twitter API credentials
with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['API_KEY']
    consumer_secret = info['API_SECRET']
    access_key = info['ACCESS_TOKEN_KEY']
    access_secret = info['ACCESS_TOKEN_SECRET']

# Create the API endpoint
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Mention the maximum number of tweets that you want to be extracted.
max_number_of_tweets_to_be_extracted = int(input('Enter the number of tweets that you want to extract: '))

# Mention the hashtag that you want to look out for
ticker = input('Enter the hastag that you want to scrape for: ')
"""
for tweet in tweepy.Cursor(api.search, q='#' + ticker, rpp=100).items(max_number_of_tweets_to_be_extracted):
    with open('tweets_with_hashtag_' + hashtag + '.txt', 'a') as the_file:
        the_file.write(str(tweet.text.encode('utf-8')) + '\n')
"""

# Function scrapes twitter API to look for tweets that have specific ticker symbol based on user input.
def getTweets():
    for tweet in tweepy.Cursor(api.search, q='$' + ticker, rpp=100).items(max_number_of_tweets_to_be_extracted):
        current_tweet = tweet.text.encode('utf-8')
        tweets.append(current_tweet)

# Function checks if the tweet has a url and if so, it appends that link to a list.
def links2list():
    for tweet in tweets:
        searchString = "(?P<url>https?://[^\s]+)"
        link = re.search(searchString, tweet.decode("utf-8"))
        if link:
            links.append(link)

# Function opens all the links form the links list in new tabs in Google Chrome.
def openLinksInChrome():
    for link in links:
        url = link.group(0)
        webbrowser.open_new_tab(url)

# Specify global empty lists.
tweets = []
links = []

# Run the code.
getTweets()
links2list()
openLinksInChrome()

# Print a results statement that shows how many links were extracted from the specified number of tweets.
print('Extracted ' + str(len(links)) + ' links from ' + str(max_number_of_tweets_to_be_extracted) + ' tweets with ticker $' + ticker)
