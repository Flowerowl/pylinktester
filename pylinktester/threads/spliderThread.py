#!/usr/bin/env python   
# -*- coding: utf-8 -*-
import threading
import sys
sys.path.insert(0, r'..')
import core.bfs as core

'''
爬虫线程
采用广度优先算法
'''
class spliderThread(threading.Thread):
	def __init__(self, urlQuence, urlSync, deepth, mutex):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		#保存爬取链接的集合
		self.urlQuence = urlQuence
		#同时需要更新的供检测线程使用的队列
		self.urlSync = urlSync
		#爬取深度
		self.deepth = deepth
		self.mutex = mutex

	def run(self):
		core.bfs(self.urlQuence, self.urlSync, self.deepth, self.mutex)
