#!/usr/bin/python3
"""
Script queries number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """ Returns total number of subscribers for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Google Chrome Version 127.0.6533.100'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers')
    else:
        return 0
