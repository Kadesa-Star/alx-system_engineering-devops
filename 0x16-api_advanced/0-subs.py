#!/usr/bin/python3
"""
Module querying Reddit API to get no of subscribers for subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API to return no of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit,
        or 0 if invalid or error.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MyRedditAgent/1.0)'
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
