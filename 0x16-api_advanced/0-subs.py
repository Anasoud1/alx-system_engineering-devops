#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    if subreddit is None:
        return (0)
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 123.0.6286.0'}
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        return data.get('data').get('subscribers')
    except Exception:
        return 0
