from bs4 import BeautifulSoup
import time
import datetime
import logging

from pizzagate_V1.modules.truepundit import TruepunditDP, TruepunditIP

class SteemitDP(TruepunditDP):	
	def steemit_main(self):
		'''
		Output: CSS selectors for article information for Steemit.
		'''
		article_selector = 'article'
		date_time = self.soup.select('div[class="PostFull__header"] span[class="updated"]')[0]['title']
		unixtime = time.mktime(datetime.datetime.strptime(date_time, "%m/%d/%Y %I:%M %p").timetuple())
		title_selector = 'h1[class="entry-title"]'
		author_selector = 'a[class="ptc"]' 
		links_selector = 'p a'
		likes = self.soup.select('article span[class="Voting"] > div > a > span')[0].get_text()
		has_more = True
		
		return (article_selector, date_time, unixtime, title_selector, author_selector, links_selector, likes, has_more)			

class SteemitIP(TruepunditIP):
	def steemit_instance(self):
		'''
		Output: Xpaths for instance information for Steemit.
		'''
		
		instance_xpath = '//div[@class=""]'
		datetime_xpath = './/span[@class="updated"]/@title'
		content_html_xpath = './/div[contains(@class, "Comment__body")]'
		author_xpath = './/a[@class="ptc"]/text()'
		likes_xpath = './/span[@class="Voting"]/div/a/span/text()'
		links_contained_xpath = './/p/a/@href'
		id_xpath = './/a[@class="ptc"]/text()'
		reply_to_xpath = '//reply'
		
		return (instance_xpath, datetime_xpath, content_html_xpath, author_xpath, likes_xpath, links_contained_xpath, id_xpath, reply_to_xpath)		