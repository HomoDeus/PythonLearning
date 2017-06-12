#coding=utf-8
#用于从百度获取数据的爬虫程序
import urllib
url="http://www.baidu.com"
print urllib.urlopen(url).read()
