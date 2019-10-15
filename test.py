import urllib.request
import re
import os
import random
import time

url = 'https://blog.csdn.net/weixin_40490238'
# 模拟浏览器
headers = ("user-agent",
           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]  # 添加报头
urllib.request.install_opener(opener)  # 设置opner全局化
# 获取网页信息
data = urllib.request.urlopen(url).read().decode('utf-8')
# 设置正则
pat = '<a href="(.*?)" target="_blank">'
# 匹配正则
res = re.compile(pat).findall(data)


def csdn():
    b = random.randint(1, len(res) - 1)
    print(b)
    print(len(res))
    os.system("curl " + res[b])
    time.sleep(1)


while True:
    csdn()
