#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts"""
from requests import get


def top_ten(subreddit):
    """ listed for a given subreddit"""
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    headers = {"User-Agent": "reddit API"}
    data = get(url, headers=headers, allow_redirects=False)
    if data.status_code is not 200:
        return print(None)
    redd = data.json().get("data").get("children")
    for item in redd:
        print(item.get("data").get("title"))
