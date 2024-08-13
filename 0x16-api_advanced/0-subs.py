#!/usr/bin/python3
"""
Script that queries the number of subscribers
for a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if the
        subreddit is invalid or an error occurs.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; RedditSubChecker/1.0)'
        }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
