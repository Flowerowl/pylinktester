#!/usr/bin/env python
# -*- coding: utf-8 -*-
import model.urlQuence as urlQuence
import threads.threadController as tc
import model.urlSync as urlSync


if __name__=="__main__":
	seed = set(["http://lazynight.me"])	#初始url,算作第一层链接
	threadNumber = 10	#线程数
	deepth = 5	#设置爬取深度
	urlQuence = urlQuence.urlQuence(deepth+1)	#初始化deepth个set，存放相应层数未访问链接
	urlQuence.addUnvisitedUrl(seed, 1)	#seed链接算作第一层
	urlSync = urlSync.urlSync() #为testThread同步未访问的url集合
	tc = tc.threadController(threadNumber, urlQuence, urlSync, deepth)	#初始化线程管理器
	tc.start()
