import requests

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
