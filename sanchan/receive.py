# -*- coding: utf-8 -*-
import re

def pattern_match(patterns, text):
	for p in patterns.iterkeys():
		match = re.search(p, text)
		if match:
			p_type = patterns[p]
			if p_type == 'today':
				count = int(match.group(2))
				return u"サンちゃんは今日%d回ナンパされたそうです。" % count
			elif p_type == 'once':
				return u"サンちゃんがただ今ナンパされています。"
			else:
				return False

# Test code here.
if __name__ == "__main__":
	patterns = {
		u'ナンパされたなう': 'once',
		u'(今日は|今日|)(\d+)回(も|)ナンパされ(た|ました)': 'today'
	}
	texts = [
		u'ナンパされたなう',
		u'今日は1回ナンパされました',
		u'やべえ、今日2回ナンパされた',
		u'3回もナンパされた件ｗｗｗ',
		u'なんでもない'
	]
	for t in texts:
		print pattern_match(patterns, t)
