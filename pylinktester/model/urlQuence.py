#!/usr/bin/env python
# -*- coding: utf-8 -*-

global uv

class urlQuence:
    '''
    爬虫线程的链接保存集合，按层分配，一层一个set()
    '''

    def __init__(self, deepth):
        #已访问的url集合
        self.visited=set()
        #设定爬去深度
        self.deepth = deepth
        #未访问的url字典，按层数做key
        self.unVisited = {}

        for i in range(self.deepth):
            self.unVisited[i+1] = set()

    #获取访问过的url集合
    def getVisitedUrl(self):
        return self.visited
    #获取未访问的url集合
    def getUnvisitedUrl(self):
        uv = set()
        for i, s in self.unVisited.items():
            uv |= s
        return uv
    #添加到访问过得url队列中
    def addVisitedUrl(self, url):
        self.visited.add(url)
    #移除访问过得url
    def removeVisitedUrl(self, url):
        self.visited.remove(url)
    #按层提取未访问过得url
    def unVisitedUrlDeQuence(self, deepth):
        try:
            return self.unVisited[deepth].pop()
        except:
            return None
    #按层插入未访问url
    def addUnvisitedUrl(self, url, deepth):
        self.unVisited[deepth].update(url)
    #获得已访问的url数目
    def getVisitedUrlCount(self):
        return len(self.visited)
    #获得未访问的url数目
    def getUnvistedUrlCount(self):
        count = 0
        for i in range(self.deepth):
            count += len(self.unVisited[i+1])
        return count
    #获取指定层数未访问链接数目
    def getUnvisitedUrlCountByDeepth(self, deepth):
        return len(self.unVisited[deepth])
    #判断未访问的url集合是否为空,返回最小非空层
    def getLayerunVisited(self):
        for i in range(self.deepth):
            if len(self.unVisited[i+1]) != 0:
                return i+1


