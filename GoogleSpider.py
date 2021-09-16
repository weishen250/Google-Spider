import re
import urllib
import requests
from bs4 import BeautifulSoup
import urllib3
import time

#  正则匹配表达式 http\D*?://\D*?/

urllib3.disable_warnings()  # 忽略https证书告警

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"


# query为搜索内容
# query = input("请输入需要搜索的谷歌命令：")
# num为一次搜索的数量
def search(query,page):
    num = 1
    query = query.replace(' ', '+')
    for num in range(page):
        URL = f"https://www.google.com.hk/search?q={query}&newwindow=1&hl=zh-CN&ei=MSEaYcmdH9TW-QaTr7aIBg&start={num}&sa=N&ved=2ahUKEwiJ-vanj7XyAhVUa94KHZOXDWE4FBDw0wN6BAgBEEU&biw=1366&bih=773"

        try:

            headers = {"user-agent": USER_AGENT}
            proxy = {'http':'127.0.0.1:7890'}
            resp = requests.get(URL, headers=headers, verify=False,proxies=proxy)
            time.sleep(0.1)

            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, "html.parser")

                results = []

                # url在<div>标签下的<a>标签下的href值里
                for g in soup.find_all('div'):  # <div>
                    anchors = g.find_all('a')  # <a href="">
                    if anchors:
                        for i in range(len(anchors)):
                            try:
                                link = anchors[i].attrs['href']  # 提取字典内容

                                # 正则过滤URL，删除掉一些乱码
                                if re.match('/', link) is None and re.match('(.*)google.com',
                                                                            link) is None and link != '#' and link.find(
                                    'search?q') == -1:

                                    # 过滤掉重复的URL
                                    for i in results:
                                        if i.split(".site")[0] == link.split(".site")[0]:
                                            link = ""
                                    results.append(link)
                            except:
                                pass
                        # print(anchors[0].attrs['href'])



            # 写入文件
            with open(f"./result/{query}.txt",mode="a+") as f:
                for i in results:
                    if i != '':
                        print(results)
                        f.write(i + "\n")
        except:
            print('发现错误，已自动跳过')

