#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r'..')
import threading
import utils.testUrls as utils

'''
检测链接的调度器
'''
def test(urlSync, spliderThreadPool, mutex):
    while urlSync.getUnvistedUrlCount() != 0 or spliderIsAlive(spliderThreadPool):
        #print "test-mutex.acquire()..."
        mutex.acquire()
        #print "test-mutex.acquire() OK"
        url = urlSync.getUnvisitedUrl()
        mutex.release()
        #print "test-mutex.release() OK"
        if url in urlSync.visited:
            continue
        if url is None:
            print '剩余链接数量',urlSync.getUnvistedUrlCount()
            for st in spliderThreadPool:
                print st.getName(),st.isAlive()
            continue
        print threading.currentThread()
        #检测链接
        utils.testUrls(url)
        #print "test-2-mutex.acquire()..."
        mutex.acquire()
        #print "test-2-mutex.acquire()OK"
        urlSync.addVisistedUrl(url)
        mutex.release()
        #print "test-2-mutex.release()OK"
        print '剩余链接数量',urlSync.getUnvistedUrlCount()

'''
判断爬虫是否已死
'''
def spliderIsAlive(spliderThreadPool):
    for st in spliderThreadPool:
        if st.isAlive():
            return True
    return False
