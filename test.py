# -*- coding: utf-8 -*-
# python3.6
import random
import ssl
import urllib3
from time import mktime, asctime, localtime

import requests


def get_name():
    xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
    X = random.choice(xing)
    M = "".join(random.choice(ming) for i in range(2))
    return X + M


def get_birthday():
    # mktime(tuple)讲时间元组转换为本地时间
    # 日期元组说明：年，月，日，时，分，秒，周，儒历日，夏令时
    date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
    time1 = mktime(date1)
    date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
    time2 = mktime(date2)
    # 在这一范围内生成随机数
    random_time = random.uniform(time1, time2)  # uniform返回随机实数 time1 <= time < time2
    # localtime(seconds)将秒数转换为日期元组
    # asctime([tuple]) 将时间元组转换为字符串
    print(asctime(localtime(random_time)))


def qrcode():
    headers = {
        'Host': 't.mdingvip.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6',
    }

    params = (
        ('__dmt', '3230862c6fd429f85a3a602b4a808f5b'),
        ('tcode', '1025'),
    )

    ssl._create_default_https_context = ssl._create_unverified_context
    response = requests.get('http://t.mdingvip.com/jump/', headers=headers, params=params, verify=False)
    result = response.headers
    print(result)


if __name__ == '__main__':
    # print(get_name())
    # get_birthday()
    # a = '中国'
    # print(quote(a))
    qrcode()
