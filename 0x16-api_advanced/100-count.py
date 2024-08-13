#!/usr/bin/python3
"""
Module for querying Reddit API and counting keyword occurrences in titles.
"""

import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list, hot_list=None, after=None):
    """
    Queries the Reddit API, parses titles of all hot articles, and counts
    occurrences of given keywords in a case-insensitive manner.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        hot_list (list): Accumulates hot post titles (used for recursion).
        after (str): Parameter for pagination (used for recursion).

    Returns:
        None: Prints sorted count of each keyword.
    """
    if hot_list is None:
        hot_list = []

    user_agent = {
        'User-Agent': 'Google Chrome Version 127.0.6533.100'
    }
    url = (
        f'https://www.reddit.com/r/{subreddit}/hot/.json?after={after}'
    )
    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after')

        for item in children:
            title = item.get('data', {}).get('title', '')
            hot_list.append(title.lower())

        if after:
            count_words(subreddit, word_list, hot_list, after)
        else:
            # Process the accumulated hot_list
            word_count = defaultdict(int)
            word_pattern = re.compile(r'\b\w+\b', re.IGNORECASE)

            for title in hot_list:
                for word in word_list:
                    matches = word_pattern.findall(title)
                    word_count[word] += matches.count(word.lower())

            # Print the results
            sorted_words = sorted(
                word_count.items(),
                key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")

    except Exception:
        pass
