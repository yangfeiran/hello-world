# -*- coding: utf-8 -*-
import urllib
import re

url1 = "http://finance.sina.com.cn/"
url2 = "http://finance.baidu.com/"
url3 = "http://finance.qq.com/"
url4 = "http://money.163.com/"
url5 = "http://www.hao123.com/stocknew"
url6 = "http://www.eastmoney.com/"
url7 = "http://www.stockstar.com/"
url8 = "http://www.cnfol.com/"
url9 = "http://www.cnstock.com/"
url10 = "http://www.hexun.com/"
url11 = "http://finance.ifeng.com/"
url12 = "http://business.sohu.com/"
url13 = "http://www.caijing.com.cn/"
url14 = "http://www.cfi.net.cn/"
url15 = "http://www.ce.cn/"

urllist = [url3]
x = 0
#file_object = open("test1.txt", 'a')
file_obj = open("test2.txt", 'a')
reg = ur'(<a.{0,20}href="http.{0,100}".{0,20}target="_blank">.{0,20}[\u6DA8|\u591A|\u5347|\u8FDB|\u7EA2|\u5E72]+.{0,20}</a>)'
mat = re.compile(reg)
#rereg = ur'([\u4e00-\u9fa5]+)'
#remat = re.compile(rereg)

for url in urllist:
	response = urllib.urlopen(url)
	html = response.read().lower().decode("gbk")
	list = re.findall(mat, html)

	for ma in list:
		file_obj.write(ma.encode('utf8'))
		file_obj.write('\r')
		x += 1
		#one = re.findall(remat, ma)
		#for reone in one:
		#	file_object.write(reone.encode("utf8"))
		#	file_object.write('\r')

print x
file_obj.close()
#file_object.close()