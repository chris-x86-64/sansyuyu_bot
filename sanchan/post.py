class NormalTweet():
	def __init__(self, api):
		self.api = api

	def post(self, content, in_reply_to_status_id):
		self.api.update_status(content, in_reply_to_status_id)

	def retweet(self, status_id):
		self.api.retweet(id = status_id)
