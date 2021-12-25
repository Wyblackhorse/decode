import requests

cookies = {
    'UM_distinctid': '17df0acff6e5f6-0129409c3b6b54-5437971-3d10d-17df0acff6fbc0',
    'CNZZDATA1278650834': '1847589092-1640419158-%7C1640419158',
    'Hm_lvt_4b4ce93f1c92033213556e55cb65769f': '1640420409',
    'Hm_lpvt_4b4ce93f1c92033213556e55cb65769f': '1640420409',
    'sid1': '1640420409852-4D0C8C2C7B32959E08C0CDDD70A63EB6',
    'sid2': '1640420409852-4D0C8C2C7B32959E08C0CDDD70A63EB6',
    'pvid': '1',
    'mvid': 'cd1bce69-dd0e-46a5-997f-e1943803a6d8',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('userName', '892368376@qq.com'),
    ('password', 'g+eCSeWRLcDfhe4ezU78LQ=='),
    ('referrer', 'wap'),
    ('mainVersion', '300021100'),
    ('comParam_curTime', '1640420657669'),
    ('comParam_seqCode', '064054D35E9F5D8E8F183E3FDBF713DF'),
    ('comParam_signature', 'b8fe1a6e7852651b091ea6cf5acb01e3'),
    ('isCheck', 'true'),
    ('locale', 'zh-cn'),
)

response = requests.get('https://m.ctyun.cn/account/login', headers=headers, params=params, cookies=cookies)

print(response.text)

