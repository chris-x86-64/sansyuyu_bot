# -*- coding: utf-8 -*-

import tweepy

class StreamListener(tweepy.StreamListener):
	def on_connect(self):
		print "[INFO] Initiating connection to twitter.com"

	def on_status(self, status):
		try:
			print status.text
			return
		except:
			pass

	def on_error(self, code):
		print code
		return False

class Stream(tweepy.Stream):
	def __init__(self, oauth):
		listener = StreamListener()
		super(Stream, self).__init__(auth = oauth, listener = listener)
