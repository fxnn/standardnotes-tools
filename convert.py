#!/usr/bin/python

import sys
import json
import sncore

if len(sys.argv) != 2:
	print "usage: %s directory" % sys.argv[0]
	exit()
directory = sys.argv[1]

items = sncore.items_from_dir(directory)
json.dump({"items": items}, sys.stdout)

