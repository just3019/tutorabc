# -*- coding: utf-8 -*-
# python3.6
import random
import ssl

import datetime
import time

import requests


def get_name():
    xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
    X = random.choice(xing)
    M = "".join(random.choice(ming) for i in range(2))
    return X + M


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


def genBthy(n):
    t = int(time.time())
    tt = t - (datetime.timedelta(days=365) * n).total_seconds()
    r = random.randrange(tt, t)
    bthy = datetime.date.fromtimestamp(r)
    return bthy.strftime(random.choice(["%Y-%m-%d"]))


def get_sex():
    ran = random.randint(1, 2)
    print(str(ran))
    return str(ran)


if __name__ == '__main__':
    # print(genBthy(20))
    pro = ['123.163.27.70:8118', "123.180.68.152:8010", "1.196.161.222:9999", "183.159.93.232:18118"]
    proxy = {"https": "https://" + random.choice(pro)}
    print(str(proxy))
