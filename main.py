import os
import GoogleSpider
import ReRuls
import ReadTitile

global query

isExists=os.path.exists('result')
if not isExists:
	os.makedirs('result') 


query = input("请输入需要搜索的谷歌命令：")

page = int(input("请输入需要爬行的页数："))

GoogleSpider.search(query,page)
ReRuls.clear(query)
ReadTitile.load(query)