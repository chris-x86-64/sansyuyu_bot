from tweepy import OAuthHandler

class SanchanOAuthHandler():
	def __init__(self, config):
		keys = config.OAuthKeys()
		self.oauth = OAuthHandler(keys['consumer_key'],
				keys['consumer_secret'],
				secure = True
				)
		self.oauth.set_access_token(keys['access_token_key'], keys['access_token_secret'])

	def authenticate(self):
		return self.oauth
