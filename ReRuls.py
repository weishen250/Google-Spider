import re
from bs4 import BeautifulSoup
import requests
import urllib3
import threading
from requests.exceptions import HTTPError
import csv

# re.search()
# 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
# re.match()
# 从一个字符串的开始位置起匹配正则表达式，返回match对象
# re.findall()
# 搜索字符串，以列表类型返回全部能匹配的字符串
# re.split()
# 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
# re.finditer()
# 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
# re.sub()
# 字啊一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
def clear(query):
    result = []

    for url in open(f'./result/{query}.txt',mode='r+',encoding='utf-8') :

        try:
            host = re.findall(r'http\D*?://\D*?/',url)[0]
            #host = url.split(url+'\n')
            #print(host)

            fp = open(f'./result/c{query}.txt', mode='a+', encoding='utf-8')

            if host not in result:
                result.append(host)
            fp.write(host+'\n')

            print(host)



        except :
            print("*"*20)

    print('URL简化结束，即将开始title识别')




# urllib3.disable_warnings()  # 忽略https证书告警
# # desktop user-agent
# USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# headers = {"user-agent": USER_AGENT}
# results = []
# ts = []
#
#
# def check_if_live(url: str, timeout: float) -> bool:
#     try:
#         res = requests.get(url, headers=headers, verify=False, timeout=timeout)
#
#         if res.status_code == 200:
#
#             soup = BeautifulSoup(res.content, "html.parser")
#             name = soup.find('title').text
#             title = name.replace('<title>','').replace('</title>','')
#             # print(url)
#             # print(title)
#
#
#             # results.append(url)
#             # results.append(title)
#             # with open('test.csv', 'a+')as f:
#             #     f_csv = csv.writer(f)
#             #     f_csv.writerow(results)
#             #
#             print(results)
#             # results.clear()
#     except:
#         print('出现错误')
#     return True
#
#
# def __handler(line: str):
#     check_if_live(line, 0.7)
#
#
# with open("curls.txt", "r") as f:
#     for line in f:
#         line = line[:-1]
#         t = threading.Thread(target=__handler, args=(line,))
#         t.start()
#         ts.append(t)
#
# for t in ts:
#     t.join()
#
# with open("huourls.txt", "w") as f:
#     for i in results:
#         f.write(i + "\n")