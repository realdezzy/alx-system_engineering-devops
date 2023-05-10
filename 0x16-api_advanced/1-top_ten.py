#!/usr/bin/python3
# Hot Posts
"""Returns title of 10 hot posts for a subreddit"""
import requests


def top_ten(subreddit: str):
    """ Hot post title """
    count = requests.get("https://www.reddit.com/r/{}/top.json?limit=10"
                         .format(subreddit))
    obj = count.json()
    children = obj["data"]["children"]

    for i in children:
        print(i["data"]["title"])
