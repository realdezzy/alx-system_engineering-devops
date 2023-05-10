#!/usr/bin/python3
""" Keywords Count """
import requests


def count_words(subreddit, keywords, after=None, counts=None):
    """ Keyword Count """
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if not data.get('data') or not data['data'].get('children'):
        return counts
    for child in data['data']['children']:
        title = child['data']['title'].lower()
        for keyword in keywords:
            if keyword in title:
                counts[keyword] = counts.get(keyword, 0) + 1
    next_after = data['data']['after']
    if next_after:
        counts = count_words(subreddit, keywords,
                             after=next_after, counts=counts)
    else:
        for x, y in sorted(counts.items()):
            print("{}: {}".format(x, y))
