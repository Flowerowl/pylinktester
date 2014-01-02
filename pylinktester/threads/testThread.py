#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import sys
sys.path.insert(0, r'..')

import core.test as core

class testThread(threading.Thread):
    '''
    检测线程
    '''

	def __init__(self, urlSync, spliderThreadPool, mutex):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		#链接队列
		self.urlSync = urlSync
		#爬虫线程池，用来检测爬虫是否已死
		self.spliderThreadPool = spliderThreadPool
		self.mutex = mutex

	def run(self):
		core.test(self.urlSync, self.spliderThreadPool, self.mutex)
