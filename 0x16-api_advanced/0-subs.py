#!/usr/bin/python3
"""
Script that queries the number of subscribers
for a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
            'User-Agent': 'RedditSubChecker/1.0 (Kadesa)'
        }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0
