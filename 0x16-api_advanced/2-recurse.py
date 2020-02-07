#!/usr/bin/python3

import requests
import itertools


def recurse(subreddit, hot_list=[], after=None):
    '''returns a list containing the titles of all hot article'''

    if after is None:
        url = 'https://reddit.com/r/{}/hot/.json?limit=100'.format(subreddit)
    else:
        url = 'https://reddit.com/r/{}/hot/.json?limit=100&after={}'.format(
              subreddit, after)

    headers = {'User-Agent': 'x'}
    req = requests.get(url, headers=headers).json()

    try:
        check = req.get('data').get('children')
    except AttributeError:
        return None

    after = req.get('data').get('after')
    posts = req.get('data').get('children')
    titles = list(map(lambda x: x.get('data').get('title'), posts))
    hot_list.append(titles)

    if after is None:
        return list(itertools.chain(*hot_list))
    else:
        return recurse(subreddit, hot_list, after)
