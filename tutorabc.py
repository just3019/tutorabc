# -*- coding: utf-8 -*-
# python3.6

import json
import random
from urllib import parse, request
import time
import re
from urllib.parse import quote
import datetime

import requests

header_dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}

TOKEN = '00499849cbf687835af75182698438eb3c2ccdf4'  # 输入TOKEN
ITEMID = '15887'  # 项目编号
EXCLUDENO = ''  # 排除号段170_171
MOBILE = ''  # 手机号
code = ''  # 验证码
__tkpm__ = ''
phpsessid = ''
location = ''
server = 'http://180.119.53.85:26189'


def log(s):
    f = open(file_path, "a")
    f.write('%s\n' % s)
    f.close()


def get_sex():
    ran = random.randint(1, 2)
    print(str(ran))
    return str(ran)


def genBthy(n):
    t = int(time.time())
    tt = t - (datetime.timedelta(days=365) * n).total_seconds()
    r = random.randrange(tt, t)
    bthy = datetime.date.fromtimestamp(r)
    return bthy.strftime(random.choice(["%Y-%m-%d"]))


def qrcode():
    headers = {
        'Host': 't.mdingvip.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6',
    }

    params = (
        ('__dmt', '3230862c6fd429f85a3a602b4a808f5b'),
        ('tcode', '1025'),
    )
    session = requests.session()
    resp = session.get('http://t.mdingvip.com/jump/', headers=headers, params=params, allow_redirects=False)
    global location
    location = resp.headers['Location']
    print(location)

    response = session.get(location)
    print(response.cookies["PHPSESSID"])
    global phpsessid
    phpsessid = response.cookies["PHPSESSID"]
    result = response.text
    global frm
    global __tkpm__
    frm = location[location.find("frm") + 4: location.find("frm") + 7]
    __tkpm__ = location[location.find("__tkpm__") + 9: location.find("__tkpm__") + 45]
    print(frm)
    print(__tkpm__)

    global token
    global tsid
    token = result[result.find("token") + 6: result.find("token") + 38]
    tsid = result[result.find("tsid") + 5: result.find("tsid") + 15]
    print("token:" + token)
    print("tsid:" + tsid)


def get_name():
    xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
    X = random.choice(xing)
    M = "".join(random.choice(ming) for i in range(2))
    return X + M


def get_phone():
    # 获取手机号码
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token=' + TOKEN + '&itemid=' + ITEMID + '&excludeno=' + EXCLUDENO
    MOBILE1 = request.urlopen(request.Request(url=url, headers=header_dict)).read().decode(encoding='utf-8')
    if MOBILE1.split('|')[0] == 'success':
        global MOBILE
        MOBILE = MOBILE1.split('|')[1]
        print('获取号码是:\n' + MOBILE)
    else:
        print('获取TOKEN错误,错误代码' + MOBILE1)
        raise RuntimeError("手机号获取不到")


def get_random():
    ran = random.randint(10, 255)
    print(str(ran))
    return str(ran)


def get_code():
    # 获取短信，注意线程挂起5秒钟，每次取短信最少间隔5秒
    WAIT = 60  # 接受短信时长60s
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=' + TOKEN + '&itemid=' + ITEMID + '&mobile=' + MOBILE + '&release=1'
    text1 = request.urlopen(request.Request(url=url, headers=header_dict)).read().decode(encoding='utf-8')
    TIME1 = time.time()
    TIME2 = time.time()
    ROUND = 1
    while (TIME2 - TIME1) < WAIT and not text1.split('|')[0] == "success":
        time.sleep(2)
        print(text1)
        text1 = request.urlopen(request.Request(url=url, headers=header_dict)).read().decode(encoding='utf-8')
        TIME2 = time.time()
        ROUND = ROUND + 1

    ROUND = str(ROUND)
    if text1.split('|')[0] == "success":
        text = text1.split('|')[1]
        TIME = str(round(TIME2 - TIME1, 1))
        print('短信内容是' + text + '\n耗费时长' + TIME + 's,循环数是' + ROUND)
    else:
        print('获取短信超时，错误代码是' + text1 + ',循环数是' + ROUND)
        raise RuntimeError("获取验证码失败")

    # 释放号码
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=release&token=' + TOKEN + '&itemid=' + ITEMID + '&mobile=' + MOBILE
    RELEASE = request.urlopen(request.Request(url=url, headers=header_dict)).read().decode(encoding='utf-8')
    if RELEASE == 'success':
        print('号码成功释放')
    # # 拉黑号码
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=addignore&token=' + TOKEN + '&itemid=' + ITEMID + '&mobile=' + MOBILE
    BLACK = request.urlopen(request.Request(url=url, headers=header_dict)).read().decode(encoding='utf-8')
    if BLACK == 'success':
        print('号码拉黑成功')

    # 提取短信内容中的数字验证码
    pat = "[0-9]+"
    IC = 0
    IC = re.search(pat, text)
    if IC:
        global code
        code = IC.group()
        print("验证码是:\n" + IC.group())
    else:
        print("请重新设置表达式")
        raise RuntimeError("验证码提取失败")


def login():
    import requests

    cookies = {
        'PHPSESSID': phpsessid,
    }

    headers = {
        'Host': 'p.viplex.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-cn',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://p.viplex.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 MicroMessenger/6.7.1 NetType/WIFI Language/zh_CN',
        'Referer': location,
    }

    global MOBILE
    global code
    data = 'frm=x01&__tkpm__=' + __tkpm__ + '&chanid=&need_bx=0&need_loan=0&name=' + quote(
        get_name()) + '&sex=' + get_sex() + '&birthday=' + genBthy(
        30) + '&mobile=' + MOBILE + '&checknum=' + code + '&addagree=1'
    response = requests.post('https://p.viplex.cn/html/vipabc/', headers=headers, cookies=cookies, data=data)
    print("登录信息：" + response.text)
    result = json.loads(response.text)
    if result['status'] != 0:
        raise RuntimeError("登录失败")
    else:
        return result


def deal():
    get_phone()
    qrcode()
    send_code()
    get_code()
    login()


def get_proxy():
    session = requests.session()
    proxy = {
        'http': 'http://101.236.22.141:8866',
        'https': 'http://101.236.22.141:8866',
    }

    response = session.get(
        "http://47.106.180.108:8081/Index-generate_api_url.html?packid=7&fa=5&qty=1&port=1&format=txt&ss=1&css=&pro=&city=",
        proxies=proxy)
    result = response.text
    print(result)
    return result


# 发送验证码
def send_code():
    cookies = {
        'PHPSESSID': phpsessid,
    }

    headers = {

    }

    params = (
        ('do', 'sendcode'),
        ('mobile', MOBILE),
        ('token', token),
        ('tsid', tsid),
        ('random', random.random),
    )

    pro = ["http://101.236.22.141:8866", "http://222.188.180.238:31717", "http://219.156.162.113:33983"]

    # print(params)
    # server = random.choice(pro)
    global server
    proxy = {
        'http': server,
        'https': server
    }

    # proxy1 = {'http': 'http://117.93.120.134:33131',
    #           'https': 'http://117.93.120.134:33131'}

    print(proxy)
    session = requests.session()
    try:
        response = session.get('https://p.viplex.cn/html/vipabc/vipabc.php', headers=headers, params=params,
                               cookies=cookies, proxies=proxy)
        print(response.text)
    except:
        # server = get_proxy()
        raise RuntimeError("发送验证码失败")
    print("发送验证码：" + response.text)
    result = json.loads(response.text)['status']
    if result == 2:
        server = get_proxy()
        raise RuntimeError("验证码发送太频繁")


if __name__ == '__main__':
    index = 0
    global file_path
    file_path = '%s.txt' % time.strftime("%Y%m%d")
    while index < 4:
        print(index)
        try:
            deal()
            index += 1
            log(MOBILE)
        except RuntimeError as e:
            # 释放号码
            url = 'http://api.fxhyd.cn/UserInterface.aspx?action=release&token=' + TOKEN + '&itemid=' + ITEMID + '&mobile=' + MOBILE
            RELEASE = request.urlopen(request.Request(url=url, headers=header_dict)).read().decode(encoding='utf-8')
            if RELEASE == 'success':
                print('号码成功释放')
            # # 拉黑号码
            url = 'http://api.fxhyd.cn/UserInterface.aspx?action=addignore&token=' + TOKEN + '&itemid=' + ITEMID + '&mobile=' + MOBILE
            BLACK = request.urlopen(request.Request(url=url, headers=header_dict)).read().decode(encoding='utf-8')
            if BLACK == 'success':
                print('号码拉黑成功')
            print(e)
        time.sleep(2)
