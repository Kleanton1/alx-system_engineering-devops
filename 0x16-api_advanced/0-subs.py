#!/usr/bin/python3
"""
queries and returns the number of subscribers from the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
	'''
	Description:
	- queries and returns the number of subscribers
	 (not active users, total subscribers) for a given subreddit.
	- returns 0 if an invalid subreddit is given
	'''
	endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
	headers = {'User-Agent': 'My User Agent 1.0'}
	res = requests.get(endpoint,headers=headers)

	if res.status_code !=200:
		return 0
	return res.json()['data']['subscribers']
