# -*- coding: utf-8 -*-

from optparse import OptionParser
from sanchan.config import Config
from sanchan.auth import SanchanOAuthHandler, Test
from sanchan.streaming import Stream
import sys

parser = OptionParser()
parser.add_option("-c", "--config", action = "store", dest = "config_file", help = "config file in yaml format.")
(options, args) = parser.parse_args()

config = Config(options.config_file)

try:
	oauth = SanchanOAuthHandler(config).authenticate()
except TypeError:
	print options.config_file + " doesn't contain OAuth keys."
	sys.exit(1)

test = Test(oauth)
test.credentials()

streamer = Stream(oauth)
try:
	streamer.filter(['166976355'])
except KeyboardInterrupt:
	print "[CRITICAL] Exiting saitan-bot on SIGINT. Good bye."
	sys.exit(0)
