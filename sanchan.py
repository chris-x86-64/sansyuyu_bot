# -*- coding: utf-8 -*-

from optparse import OptionParser
from sanchan.config import Config
from sanchan.auth import SanchanOAuthHandler
import sys

parser = OptionParser()
parser.add_option("-c", "--config", action = "store", dest = "config_file", help = "config file in yaml format.")
parser.add_option("-t", "--test-mode", action = "store_true", dest = "test_mode", default = False, help = "Post a test tweet then exit.")
(options, args) = parser.parse_args()

config = Config(options.config_file)

try:
	oauth = SanchanOAuthHandler(config).authenticate()
except TypeError:
	print options.config_file + " doesn't contain OAuth keys."
	sys.exit(1)

if options.test_mode == True:
	print "[DEBUG] Testing mode initiated."
	print "[DEBUG] Testing OAuth keys..."
	from tweepy import API, error
	api = API(auth_handler = oauth)
	try:
		me = api.me()
	except error.TweepError, e:
		print "[EMERG] Re-authentication required."
		oauth_new = SanchanOAuthHandler(config).request()

	print "[INFO] Successfully authenticated as %s!" % me.screen_name
