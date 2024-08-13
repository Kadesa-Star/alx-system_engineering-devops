#!/usr/bin/python3
"""Contains recurse function"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): Accumulates titles of hot posts.
        after (str): The parameter for pagination.
        count (int): The number of posts fetched so far.

    Returns:
        list: list titles of hotposts or None if subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36"
                )
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 404:
            return None

        results = response.json().get("data", {})
        after = results.get("after")
        count += results.get("dist", 0)

        for post in results.get("children", []):
            hot_list.append(post.get("data", {}).get("title", ""))

        if after:
            return recurse(subreddit, hot_list, after, count)
        return hot_list

    except requests.RequestException:
        return None
