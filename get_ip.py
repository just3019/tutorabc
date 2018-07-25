# IP地址取自国内髙匿代理IP网站：www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用
from bs4 import BeautifulSoup
import requests
import random


# 获取当前页面上的ip
def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text)
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
    tds = ip_info.find_all('td')
    ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


# 从抓取到的Ip中随机获取一个ip
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


# 国内高匿代理IP网主地址
url = 'http://www.xicidaili.com/nn/'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
# 计数器，根据计数器来循环抓取所有页面的ip
num = 0
# 创建一个数组，将捕捉到的ip存放到数组
ip_array = []
while num < 1537:
    num += 1
    ip_list = get_ip_list(url + str(num), headers=headers)
    ip_array.append(ip_list)
for ip in ip_array:
    print(ip)
    # 创建随机数，随机取到一个ip
    # proxies = get_random_ip(ip_list)
    # print(proxies)