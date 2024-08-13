#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: Number of subscribers or 0 if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'RedditSubChecker/1.0 (kadesa task 0)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
