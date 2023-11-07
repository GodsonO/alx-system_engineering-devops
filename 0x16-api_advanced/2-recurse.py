#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], nextpage=None, count=0):
    """Request subreddit recursively using pagination
    """
    user_agent = 'api_advanced-project'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if nextpage:
        url += '?after={}'.format(nextpage)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return None

    data = r.json()['data']

    posts = data['children']
    for post in posts:
        count += 1
        hot_list.append(post['data']['title'])

    nextpage = data['after']
    if nextpage is not None:
        return recurse(subreddit, hot_list, nextpage, count)
    else:
        return hot_list
