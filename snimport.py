
import json
import sncore

def load_items(fp):
	sndata = json.load(fp)
	if not "items" in sndata:
		print "ERROR: input data must be a dict containing an 'items' array"
		exit(1)
	return sndata["items"]

def tags_from_items(items):
	result = {}
	tag_items = [item for item in items if item["content_type"] == "Tag"]
	for item in tag_items:
		title = item["content"]["title"]
		if title in result:
			print "WARNING: input contains tag '%s' multiple times" % title
		result[title] = item
	return result

def retain_notes_and_tags(items):
	return [item for item in items if item["content_type"] == "Tag" or item["content_type"] == "Note"]

