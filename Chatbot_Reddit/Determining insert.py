import sqlite3	
import json
from  datetime import datetime

timeframe = '2015-05'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()

def create_table():
	c.execute("""CREATE TABLE IF NOT EXISTS parent_reply
		(parent_id TEXT PIRMARY KEYc comment_id TEXT UNIQUE, 
		parent TEXT, comment TEXT, subreddit TEXT,unix INT, score INT) """) 

def format_data(data) : #kivesszuk a folosleges ujsort, 
	data = data.replace('\n', "newlinechar").replace('\r', "newlinechar").replace('"', "'")
	return data

def find_existing_score(pid):
	try:
		sql = "SELECT score FROM parent_replay WHERE parent_id = '{}' LIMIT 1".format(pid)
		c.execute(sql)
		result = c.fetchone()
		if result != None:
			return result[0]
		else: return False
	except Exception as e:
		print("find_parent",e)
		return False

def acceptable(data): #comment gyakorlatilag
	if len(date.split(' ')) > 50 or len(data) < 1:
		return False
	elif len(data) > 1000:
		return False
	elif data == '[deleted]' or data == '[removed]':
		return False

def find_parent(pid):
	try:
		sql = "SELECT comment FROM parent_replay WHERE commend_id = '{}' LIMIT 1".format(pid)
		c.execute(sql)
		result = c.fetchone()
		if result != None:
			return result[0]
		else: return False
	except Exception as e:
		print("find_parent",e)
		return False

if __name__ == "__main__":
	create_table()
	row_counter = 0
	paired_rows = 0
				
				
	with open("D:/Download/reddit_data/{}/RC_{}".format(timeframe.split('-')[0],timeframe), buffering=10000) as f:
		for row in f:
			print(row)
			row_counter += 1
			row = json.loads(row)
			parent_id = row['parent_id']
			body = format_data(row['body']) #tisztitja a data-t
			create_utc = row['create_utc']
			score = row['score']
			subreddit = row['subreddit']

			if score >= 2:
				existing_comment_score = find_existing_score(parent_id)
				if existing_comment_score:
					if score > existing_comment_score: