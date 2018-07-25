import requests

cookies = {
    'PHPSESSID': 'jhpjvn5dtbshvofkiu99fp92h5',
}

headers = {
    'Host': 'p.viplex.cn',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 MicroMessenger/6.7.1 NetType/WIFI Language/zh_CN',
    'Referer': 'https://p.viplex.cn/html/vipabc/?frm=x01&__tkpm__=LV5PQW1ESUZTR01eIV8bFGVGS0BVWQ4DfQ__&tcode=1025',
    'Accept-Language': 'zh-cn',
    'X-Requested-With': 'XMLHttpRequest',
}

params = (
    ('do', 'sendcode'),
    ('mobile', '17086401457'),
    ('token', 'e626589d408c71233ca88de35f18947a'),
    ('tsid', '1532438741'),
    ('random', '0.7811268464031944'),
)

response = requests.get('https://p.viplex.cn/html/vipabc/vipabc.php', headers=headers, params=params, cookies=cookies)
print(response.text)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://p.viplex.cn/html/vipabc/vipabc.php?do=sendcode&mobile=17086401457&token=e626589d408c71233ca88de35f18947a&tsid=1532438741&random=0.7811268464031944', headers=headers, cookies=cookies)
