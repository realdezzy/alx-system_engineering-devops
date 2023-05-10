#!/usr/bin/python3
# Subscribers count
"""Returns number of subscribers to a subreddit"""
import requests


def number_of_subscribers(subreddit: str):
    """ Subreddit subscribers count """
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                         .format(subreddit),
                         allow_redirects=False)
    if response.status_code == 200:
        obj = response.json()
        subscribers = obj["data"]["subscribers"]
        return subscribers
    else:
        return 0
