#!/usr/bin/python3
"""
Module for querying Reddit API to get the number of subscribers
for a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the number of subscribers for a
    given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if
        invalid or error.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Google Chrome Version 127.0.6533.100'
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
