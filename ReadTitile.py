import re
from bs4 import BeautifulSoup
import requests
import urllib3
import threading
from requests.exceptions import HTTPError
import csv
import time
import socket

def load(query):

    urllib3.disable_warnings()  # 忽略https证书告警
    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    results = []

    f = open(f"./result/c{query}.txt", "r")
    for url in f:
        url =url.replace('\n','')

        try:
            res = requests.get(url=url, headers=headers, verify=False, timeout=8)

            if res.status_code == 200:

                soup = BeautifulSoup(res.content, "html.parser")
                name = soup.head.title.string
                title = name.replace('\r','').replace('\n','').replace('\t','').replace(' ','')

                # print(url)
                # print(name)

                host1 = url.replace('http:','').replace('https:','').replace('/','')
                # res = socket.gethostbyname(socket.gethostname(host1))
                ip = socket.gethostbyname(host1)


                results.append(url)
                results.append(title)
                results.append(ip)
                with open(f'./result/{query}.csv', 'a+',newline='')as f:
                    f_csv = csv.writer(f)
                    f_csv.writerow(results)

                print(results)
                results.clear()

        except:
            print('该站无法访问，已自动忽略。')
