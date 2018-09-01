#!/usr/bin/python3
"""queries the Reddit API and returns a list
containing the titles of all hot articles"""
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """"""

    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "reddit API"}
    data = get(url, headers=headers, allow_redirects=False)
    if data.status_code is not 200:
        return None
    redd = data.json().get("data").get("children")
    for item in redd:
        hot_list.append(item.get("data").get("title"))
    after = data.json().get("data").get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
