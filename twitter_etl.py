import pandas as pd
import tweepy

def run_twitter_etl():
    # Your Bearer Token from developer.x.com
    BEARER_TOKEN = ""  # removed from privacy reasons

    # Create a client
    client = tweepy.Client(bearer_token=BEARER_TOKEN)   #for V2 Twitter API

    # Get Virat Kohli's user ID
    user = client.get_user(username="imVkohli")
    user_id = user.data.id
    username = user.data.username  # This is 'imVkohli'

    # Fetch 20 recent tweets from the last 7 days (because V2 has the limit on tweet count or extract)
    tweets = client.get_users_tweets(
        id=user_id,
        max_results=20,  # Between 10 and 30 is fine
        tweet_fields=["created_at", "public_metrics"]  #specifies what metadata to return
    )

    # Convert to DataFrame
    tweet_list = []
    if tweets.data:
        for tweet in tweets.data:
            tweet_list.append({
                "username": username,
                "text": tweet.text,
                "created_at": tweet.created_at,
                "likes": tweet.public_metrics["like_count"],
                "retweets": tweet.public_metrics["retweet_count"]
            })

    df = pd.DataFrame(tweet_list)
    df.to_csv("s3://airflow-etl-project-01/virat_kohli_tweets.csv", index=False)
