#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import threading
import os.path
import time
import getRequest
import socket

global g_mutex
g_mutex  = threading.Lock()

'''
真正干活的检测链接函数，设置超时访问次数为三次
'''
def testUrls(url, repeat = 3):
	ti = time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime(time.time()))
	if url is not None:
		req, opener = getRequest.getRequest(url)
		try:
			urlopen = opener.open(req, timeout = 10)
		except urllib2.HTTPError, ex:
			if(repeat > 0):
				testUrls(url, repeat - 1)
			else:
				log(str(ex), ti, url)
		except urllib2.URLError, ex:
			if(repeat > 0):
				testUrls(url, repeat - 1)
			else:
				log(str(ex), ti, url)
		except socket.timeout as ex:
			if(repeat > 0):
				testUrls(url, repeat - 1)
			else:
				log(str(ex), ti, url)

'''
记录日志
'''
def log(error, ti, url):
	path = getLogsPath()
	print "log-mutex.acquire()..."
	g_mutex.acquire()
	print "log-mutex.acquire() OK"
	fileHandle = open (path+str(time.strftime('%Y-%m-%d'))+'.txt', 'a')
	fileHandle.write(ti+error+url+'\r\n')
	fileHandle.close()
	g_mutex.release()
	print "log-mutex.release() OK"

'''
获取日志路径，若没有则创建
'''
def getLogsPath():
	path = os.path.dirname(__file__)
	newpath = '/'.join(path.split('/')[:-1])+'/logs/'
	if(not os.path.exists(newpath)):
		os.mkdir(newpath)
	return newpath
