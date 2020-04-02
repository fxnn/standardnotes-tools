#!/usr/bin/python

import json
import sys

import sncore
import snexport
import snimport

if len(sys.argv) != 2:
	print "usage: %s tag_name" % sys.argv[0]
	exit()
tag_name = sys.argv[1]

items = snimport.load_items(sys.stdin)
items = snimport.retain_notes_and_tags(items)

tags = snimport.tags_from_items(items)
if tag_name in tags:
	tag = tags[tag_name]
else:
	tag = snexport.create_tag(tag_name)
	items.append(tag)

note_items = [item for item in items if item['content_type'] == "Note"]
for note in note_items:
	if sncore.FXNN_APP_ID in note['content']['appData']:
		snexport.add_reference(tag, note)
		snexport.add_reference(note, tag)
		
snexport.dump_items(items, sys.stdout)

