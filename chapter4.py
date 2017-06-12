#coding=utf-8
#Crawler for getting data from Baidu
import urllib
url="http://www.baidu.com"
print urllib.urlopen(url).read()
