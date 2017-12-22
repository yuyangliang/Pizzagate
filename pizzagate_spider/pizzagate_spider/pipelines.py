# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class PizzagateSpiderPipeline(object):
	def __init__(self):
		self.setupDBCon()
	
	def setupDBCon(self):
		self.con = sqlite3.connect('Database/test.db')
		self.cur = self.con.cursor()
		
	def closeDB(self):
		self.con.close()
		
	def __del__(self):
		self.closeDB()
	
	def process_item(self, item, spider):
		if item.__class__.__name__ == 'ArticleItem':
			self.storeInDB_article(item)
		if item.__class__.__name__ == 'InstanceItem':
			self.storeInDB_instance(item)
		return item
		
	def storeInDB_article(self, item):
		self.cur.execute(\
		"INSERT INTO article(author, url, title, datetime, domain) \
		VALUES(?, ?, ?, ?, ?)", \
		(item.get('author', ''), item.get('url', ''), item.get('title', ''), item.get('datetime', ''), item.get('domain', '') ))
		
		print 'Article Added in Database'
		self.con.commit()
		
	def storeInDB_instance(self, item):
		self.cur.execute(\
		"INSERT INTO instance(url, text_body, text_body_html, links_contained, datetime, author, id, type, likes, reply_to) \
		VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
		(item.get('url', ''), item.get('text_body', ''), item.get('text_body_html', ''), item.get('links_contained', ''), item.get('datetime', ''),  item.get('author', ''), item.get('id', ''), item.get('type', ''), item.get('likes', ''), item.get('reply_to', '')))
		
		print 'Instance Added in Database'
		self.con.commit()