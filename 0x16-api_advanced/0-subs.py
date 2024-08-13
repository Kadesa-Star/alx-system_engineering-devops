#!/usr/bin/python3
"""
Module for querying Reddit API to get the number of subscribers
for a subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API.
    - If not a valid subreddit, return 0.
    """

    if not isinstance(subreddit, str) or not subreddit:
        return 0

    url = (
        "https://www.reddit.com/r/{}/about.json".format(subreddit)
    )
    headers = {
        "User-Agent": "Google Chrome Version 127.0.6533.100"
    }
    req = get(url, headers=headers, allow_redirects=False)

    if req.status_code == 200:
        return req.json().get("data", {}).get("subscribers", 0)
    else:
        return 0
