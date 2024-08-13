#!/usr/bin/python3
"""
Module for querying Reddit API to get hot articles' titles.
"""

from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot
    articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): Accumulates titles of hot posts.
        after (str): The parameter for pagination.

    Returns:
        list: list of titles hot posts or None if subreddit invalid.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        return None

    user_agent = {'User-Agent': 'Google Chrome Version 127.0.6533.100'}

    url = (
            'https://www.reddit.com/r/{}/hot/.json?after={}'.format(
                subreddit, after
                )
            )

    try:
        response = get(url, headers=user_agent)

        if response.status_code != 200:
            return None

        all_data = response.json()
        data = all_data.get('data', {})
        children = data.get('children', [])
        after = data.get('after')

        for item in children:
            title = item.get('data', {}).get('title')
            if title:
                hot_list.append(title)

        if after is not None:
            return recurse(subreddit, hot_list, after)

        return hot_list

    except Exception:
        return None
