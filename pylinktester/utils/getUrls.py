#!/usr/bin/env python   
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import testUrls
import sys
import getRequest

reload(sys)
sys.setdefaultencoding("utf-8")

'''
获取当前页所有链接
'''
def geturls(url):
	source = getsource(url)
	urlset = set()
	try:
		soup = BeautifulSoup(source)
	except:
		return urlset
	for link in soup.find_all('a'):
		if link.get('href') is not None and (link.get('href')[:4] \
			== 'http' or link.get('href')[:1] == '/'):
			if link.get('href')[:4] == 'http':
				urlset.add(link.get('href'))
			if link.get('href')[:1] == '/':
				urlset.add('http://m.sohu.com'+link.get('href'))
	return urlset
'''
获取当前网页源码
'''
def getsource(url):
	
	req, opener = getRequest.getRequest(url)
	try:
		urlopen = opener.open(req, timeout = 10)
		source = urlopen.read()
		return source
	except Exception:
	    testUrls.testUrls(url)
