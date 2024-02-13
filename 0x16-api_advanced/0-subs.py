#!/usr/bin/python3
"""
returns the number of subscribers (not active users, total subscribers)
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers of a subreddit"""
    if subreddit is None:
        return (0)
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'API Project by anasoud'}
    r = requests.get(url, headers=headers).json()
    subscribers = r.get("data", {}).get("subscribers", 0)
    return subscribers
