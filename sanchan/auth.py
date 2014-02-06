from tweepy import OAuthHandler, error
import sys

class SanchanOAuthHandler():
	def __init__(self, config):
		self.keys = config.OAuthKeys()
		self.oauth = OAuthHandler(self.keys['consumer_key'],
				self.keys['consumer_secret'],
				secure = True
				)
		self.oauth.set_access_token(self.keys['access_token_key'], self.keys['access_token_secret'])

	def authenticate(self):
		return self.oauth

	def request(self):
		print "Authorize this app via this URL: "
		print self.oauth.get_authorization_url()
		pincode = raw_input('Then, input the proposed PIN: ')
		try:
			self.oauth.get_access_token(verifier=pincode)
		except error.TweepError, e:
			print e
			print "[EMERG] Authentication error!"
			sys.exit(1)
		print "Put these access keys into your config.yml:"
		print "access_token: " + self.oauth.access_token.key
		print "access_token_secret: " + self.oauth.access_token.secret
		sys.exit(0)
