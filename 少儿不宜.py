#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib2
import sys
from lxml import etree

print sys.argv[1]
pages=3
i=1
url='http://www.torrentkitty.net/search/%s/'%sys.argv[1]
print url
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
headers = { 'User-Agent' : user_agent }
for page in range(0,pages):
		url=url+str(i)
		i=i+1
		request = urllib2.Request(url,headers = headers)
		response = urllib2.urlopen(request)
		html=response.read()
		content=etree.HTML(html.lower().decode('utf-8'))
		mags=content.xpath("//a[@rel='magnet']")
		for mag in mags:
		    print "%s \n \n"%(mag.attrib['href'].strip('\n'))