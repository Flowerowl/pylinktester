#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r'..')
import utils.getUrls as utils
import threading

'''
广度优先算法，按层提取/存放链接
'''
def bfs(urlQuence, urlSync, deepth, mutex):
    current = urlQuence.getLayerunVisited() #当前未访问的最小层数
    while current is not None and current < deepth+1 :
        #从当前层提取一个未访问链接
        #print "bfs-mutex.acquire()..."
        mutex.acquire()
        #print "bfs-mutex.acquire() OK"
        visitUrl = urlQuence.unVisitedUrlDeQuence(current)
        mutex.release()
        #print "bfs-mutex.release() OK"
        print "第%d层未访问链接出队 \"%s\" "%(current, visitUrl)
        if visitUrl is None or visitUrl=="":
            break
        #获取超链接,set()
        links = utils.geturls(visitUrl)
        #将url放入已访问的url中
        urlQuence.addVisitedUrl(visitUrl)
        #未访问的url入列
        #print "bfs-2-mutex.acquire()..."
        mutex.acquire()
        #print "bfs-2-mutex.acquire() OK"
        urlQuence.addUnvisitedUrl(links, current+1)
        urlSync.addUnvisitedUrl(links)
        mutex.release()
        #print "bfs-2-mutex.release() OK"
        current = urlQuence.getLayerunVisited()
