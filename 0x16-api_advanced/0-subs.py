#!/usr/bin/python3
# Subscribers count
"""Returns number of subscribers to a subreddit"""
import requests


def number_of_subscribers(subreddit: str):
    """ Subreddit subscribers count """
    count = requests.get("https://www.reddit.com/r/{}/about.json"
                         .format(subreddit))
    obj = count.json()
    subscribers = obj["data"]["subscribers"]
    return subscribers
