#!/usr/bin/python3
"""
function that queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles for a given
    subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {'User-Agent': 'API Project'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        after_data = response.json().get('data').get('after')
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list, after)
        datas = response.json().get('data').get('children')
        for data in datas:
            hot_list.append(data.get('data').get('title'))
        return hot_list
    else:
        return None
