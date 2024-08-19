from textblob import TextBlob
import tweepy
import os
import sys

#before running the code you have to set up environment variable for twitter bearer_token
#go to terminal and do the following:


# Load the bearer token from an environment variable
# Load the bearer token from an environment variable
bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

# Check if the bearer token was loaded correctly
if not bearer_token:
    print("Error: Bearer token not found in environment variables.")
    sys.exit(1)

# Create a client using the bearer token
client = tweepy.Client(bearer_token=bearer_token)

# Define your search query
query = 'Python programming'

try:
    # Fetch recent tweets matching the query
    response = client.search_recent_tweets(query=query, max_results=10)

    # Print the tweets
    if response.data:
        for tweet in response.data:
            print(f"Tweet ID: {tweet.id}")
            print(f"Tweet Text: {tweet.text}")
            print('-' * 50)
    else:
        print("No tweets found.")
except tweepy.errors.Forbidden as e:
    print(f"Access error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")