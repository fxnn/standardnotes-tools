#!/usr/bin/python

import os
import sys

import json
import uuid
from datetime import datetime

import sncore

def dump_items(items, fp):
	json.dump({"items": items}, fp, indent=2)

def items_from_dir(directory):
	items = file_items_from_dir(directory, directory)
	items = items + tag_items_from_file_items(items)
	return items

def tag_items_from_file_items(file_items):
	tags = {}
	result = []
	for file_item in file_items:
		for tag in file_item['content']['appData'][sncore.FXNN_APP_ID]['tags']:
			if tag in tags:
				tag_item = tags[tag]
			else:
				tag_item = create_tag(tag)
				tags[tag] = tag_item
				result.append(tag_item)
			add_reference(tag_item, file_item)
			add_reference(file_item, tag_item)
	return result

def create_tag(title):
	return {
		"uuid": str(uuid.uuid4()),
		"created_at": datetime.now().isoformat(),
		"updated_at": datetime.now().isoformat(),
		"content_type": "Tag",
		"content": {
			"title": title,
			"references": []
		}
	}

def add_reference(item1, item2):
	item1['content']['references'].append({
		'uuid': item2['uuid'],
		'content_type': item2['content_type']
	})

def file_items_from_dir(directory, root_directory):
	result = []
	for entry_name in os.listdir(directory):
		entry_path = os.path.join(directory, entry_name)
		if os.path.isdir(entry_path):
			result += file_items_from_dir(entry_path, root_directory)
		else:
			result.append(item_from_file(entry_path, root_directory))
	return result

def item_from_file(file_path, root_directory):
	tags = tags_from_file(file_path, root_directory)
	file_name = os.path.basename(file_path)
	title, ext = os.path.splitext(file_name)
	s = os.stat(file_path)
	mtime = datetime.fromtimestamp(s.st_mtime)
	ctime = datetime.fromtimestamp(s.st_ctime)
	with open(file_path, 'r') as file:
		text_raw=file.read()
		try:
			text=text_raw.decode('utf-8')
		except UnicodeDecodeError:
			text=text_raw.decode('latin-1','ignore')
	return {
		"created_at": ctime.isoformat(),
		"updated_at": mtime.isoformat(),
		"uuid": str(uuid.uuid4()),
		"content_type": "Note",
		"content": {
			"title": title,
			"text": text.encode('utf-8'),
			"references": [],
			"appData": {
				"de.fxnn.standardnotes": {
					"original_path": file_path,
					"tags": tags + ['wikiimport']
				}
			}
		}
	}

def tags_from_file(file_path, root_directory):
	relative_path = os.path.relpath(file_path, root_directory)
	parent_dir, _ = os.path.split(relative_path)
	result = []
	while parent_dir != '':
		parent_dir, current_dirname = os.path.split(parent_dir)
		if current_dirname != '':
			result.append(current_dirname)
	return result

