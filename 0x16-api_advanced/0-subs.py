#!/usr/bin/python3
# returns the number of subscribers for a given subreddit

import requests


def number_of_subscribers(subreddit):
    '''returns the number of subscribers'''

    ep = 'https://reddit.com/r/{}.json'.format(subreddit)
    headers = {'User-Agent': 'x'}

    req = requests.get(ep, headers=headers).json()
    try:
        data = req.get('data').get('children')[0].get('data')
    except AttributeError:
        return 0
    n = data.get('subreddit_subscribers')
    return n
