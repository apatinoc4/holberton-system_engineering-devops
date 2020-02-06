#!/usr/bin/python3
# prints the titles of the first 10 hot posts


import requests


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts'''

    ep = 'https://reddit.com/r/{}.json'.format(subreddit)
    headers = {'User-Agent': 'x'}

    req = requests.get(ep, headers=headers).json()
    try:
        hot = req.get('data').get('children')
    except AttributeError:
        print('None')
        return
    for post in hot[:10]:
        print(post.get('data').get('title'))