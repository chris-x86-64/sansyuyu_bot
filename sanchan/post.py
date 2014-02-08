from tweepy import error
from random import randrange

class NormalTweet():
	def __init__(self, api):
		self.api = api

	def post(self, content, in_reply_to_status_id):
		try:
			self.api.update_status(content, in_reply_to_status_id)
		except error.TweepError:
			self.post(content + ''.join(' ' for x in range(randrange(5))), in_reply_to_status_id)

	def retweet(self, status_id):
		self.api.retweet(id = status_id)
