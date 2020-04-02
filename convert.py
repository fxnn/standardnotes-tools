#!/usr/bin/python

import sys
import json
import snexport

if len(sys.argv) != 2:
	print "usage: %s directory" % sys.argv[0]
	exit()
directory = sys.argv[1]

items = snexport.items_from_dir(directory)
snexport.dump_items(items, sys.stdout)

