#!/usr/bin/python3
""" Recursive get """
import requests


def recurse(subreddit, after=None):
    """ Recursively get hot articles from a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if not data.get('data') or not data['data'].get('children'):
        return None

    hot_list = [child['data']['title'] for child in data['data']['children']]
    next_after = data['data']['after']

    if next_after:
        more_hot_list = recurse(subreddit, after=next_after)
        if more_hot_list:
            hot_list.extend(more_hot_list)

    return hot_list
