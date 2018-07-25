import random

import requests

cookies = {
    'Hm_lpvt_7704878d2e10a1307d233598184080cb': '1532438885',
    'Hm_lvt_7704878d2e10a1307d233598184080cb': '1532438885',
    'lxInfo': '533b8r%2BqsaowsKoOs2GP1LwIjB5HltiyAjE14fc%2FIqRg9gQveMSMByG%2FSZCltxvH8IT1ZViLQH8MUhE98AhpK1c9L3zSMCaVKnASU0aqVXOEabV9bBIhs1w4vNTipwvC4kFp32LwiNBpEHUSkM6rS%2FwbD%2FjXf30H680%2F3X5AdcaVTtk',
    'PHPSESSID': 'jhpjvn5dtbshvofkiu99fp92h5',
}

headers = {
    'Host': 'p.viplex.cn',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 MicroMessenger/6.7.1 NetType/WIFI Language/zh_CN',
    'Accept-Language': 'zh-cn',
}

params = (
    ('frm', 'x01'),
    ('__tkpm__', 'LV5PQW1ESUZTR01eIV8bFGVGS0BVWAgAfw__'),
    ('tcode', '1025'),
)

response = requests.get('https://p.viplex.cn/html/vipabc/', headers=headers, params=params, cookies=cookies)
result = response.text
print(result.find("token"))
token = result[result.find("token") + 6: result.find("token") + 38]
tsid = result[result.find("tsid") + 5: result.find("tsid") + 15]
print(token)
print(tsid)
print(random.random())

# print(html)

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://p.viplex.cn/html/vipabc/?frm=x01&__tkpm__=LV5PQW1ESUZTR01eIV8bFGVGS0BVWAgAfw__&tcode=1025', headers=headers, cookies=cookies)
