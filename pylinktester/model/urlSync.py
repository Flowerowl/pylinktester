#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue

'''
为检测线程创建一个队列，同时爬虫线程向此队列添加
'''
class urlSync():
	def __init__(self):
		#链接队列
		self.urlQue = Queue.Queue()
		#已检测过的链接
		self.visited = set()
		#临时集合，用来去重
		self.tempSet = set()
	#获取未访问的链接
	def getUnvisitedUrl(self):
		try:
			return self.urlQue.get(block=True, timeout=2.0)
		except Exception, e:
			print "[EXCEPTION] getUnvisitedUrl() - EMPTY"
			return None
	#添加未访问的链接
	def addUnvisitedUrl(self, urls):
		self.tempSet.update(urls)
		for url in (self.tempSet - (self.tempSet & self.visited)):
			self.urlQue.put(url)
		self.tempSet.clear()
	#获取未访问链接数目
	def getUnvistedUrlCount(self):
		return self.urlQue.qsize()
	#获取已访问链接
	def getVisitedUrl(self):
		return self.visited
	#获取访问过的链接数目
	def getVisitedUrlCount(self):
		return len(self.visited)
	#添加已访问过的链接
	def addVisistedUrl(self, url):
		self.visited.add(url)