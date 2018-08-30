#!/usr/bin/python3
""""""
from requests import get


def number_of_subscribers(subreddit):
    """"""
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    try:
        data = get(url, headers=headers).json()
        return data['data'].get('subscribers')
    except BaseException:
        return 0
