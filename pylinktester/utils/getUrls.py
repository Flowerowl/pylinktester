#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import sys

from bs4 import BeautifulSoup

import testUrls
import getRequest

reload(sys)
sys.setdefaultencoding("utf-8")

def geturls(url):
    '''
    获取当前页所有链接
    '''
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


def getsource(url):
    '''
    获取当前网页源码
    '''
	req, opener = getRequest.getRequest(url)
	try:
		urlopen = opener.open(req, timeout = 10)
		source = urlopen.read()
		return source
	except Exception:
	    testUrls.testUrls(url)
