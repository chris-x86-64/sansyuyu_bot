# -*- coding: utf-8 -*-

import tweepy
from sanchan.receive import pattern_match
from sanchan.store import DataStore
from sanchan.post import NormalTweet
import sanchan.options

class StreamListener(tweepy.StreamListener):
	def __init__(self, oauth, patterns):
		super(StreamListener, self).__init__()
		self.patterns = patterns
		self.api = tweepy.API(auth_handler = oauth)

	def on_connect(self):
		print "[INFO] Initiated connection to twitter.com"
		print sanchan.options.config

	def on_status(self, status):
		if hasattr(status, 'text') and not hasattr(status, 'retweeted_status'):
			print u"[DEBUG] @%s: %s" % (status.user.screen_name, status.text)
			match = pattern_match(self.patterns, status.text)
			if match:
				print "[NOTICE] Pattern detected: "
				print match
				if match['message'] != 'Test code.':
					tweet_handler = NormalTweet(self.api)
					tweet_handler.retweet(status.id)
					tweet_handler.post(match['message'], None)
				with DataStore() as db_handler:
					db_handler.put(status, match['count'])

	def on_error(self, code):
		print "[EMERG] Error: " + code
		return True

class Stream(tweepy.Stream):
	def __init__(self, oauth, patterns):
		listener = StreamListener(oauth, patterns)
		super(Stream, self).__init__(auth = oauth, listener = listener)
