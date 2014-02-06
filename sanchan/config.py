import yaml
import sys

class Config():
	def __init__(self, path):
		self.path = path
		try:
			self.stream = open(self.path, 'r')
		except TypeError, e:
			print e
			print "Please specify the path to config file (--config CONFIG_FILE)"
			sys.exit(1)
		except IOError, e:
			print e
			print "Specified config file not found!"
			sys.exit(1)

		self.config = yaml.load(self.stream)

	def OAuthKeys(self):
		return self.config['oauth']
