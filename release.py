import requests
import json
import pandas as pd
import time
import os
from playwright.sync_api import sync_playwright

'''
os.remove('cookies.txt')
os.remove('cookies.json')
os.remove('data.json')
os.remove('data.xlsx')
'''

url = 'https://jwgl.wvpn.hrbeu.edu.cn/jwapp/sys/cjcx/*default/index.do?EMAP_LANG=zh#/cjcx'

with sync_playwright() as page:
    browser = page.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    context = browser.new_context()
    page.goto(url)
    time.sleep(30)
    cookies = page.context.cookies()

with open('cookies.json', 'w', encoding='utf-8') as fp:
    json.dump(cookies, fp, ensure_ascii=False)

with open('cookies.json', "r", encoding="utf-8") as n:
    data = json.load(n)
    for item in data:
        name = item.get("name")
        value = item.get("value")
        if name == 'GS_SESSIONID':
            session_id = value
        if name == '_webvpn_key':
            _webvpn_key = value
        if name == 'webvpn_username':
            webvpn_username = value
        if name == '_WEU':
            _WEU = value
        if name == 'route':
            route = value
        if name == 'JSESSIONID':
            JSESSIONID = value

header = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
 }

cookie = {
    '_WEU': _WEU,
    '_ga': 'GA1.3.438918422.1667803941',
    'route': route,
    'JSESSIONID': JSESSIONID,
    'GS_SESSIONID': session_id,
    '_webvpn_key': _webvpn_key,
    'webvpn_username': webvpn_username,
}

post = requests.post('https://jwgl.wvpn.hrbeu.edu.cn/jwapp/sys/cjcx/modules/cjcx/xscjcx.do', headers=header, cookies=cookie)
data = json.loads(post.text)

with open('data.json', 'w', encoding='utf-8') as fp:
    json.dump(data, fp, ensure_ascii=False)

num = data['datas']['xscjcx']['totalSize']
rows = data['datas']['xscjcx']['rows']

lesson_college = pd.DataFrame([rows['KKDWDM_DISPLAY'] for rows in data['datas']['xscjcx']['rows']])
lesson_name = pd.DataFrame([rows['XSKCM'] for rows in data['datas']['xscjcx']['rows']])
lesson_MAIN_score = pd.DataFrame([rows['XF'] for rows in data['datas']['xscjcx']['rows']])
lesson_level = pd.DataFrame([rows['KCXZDM_DISPLAY'] for rows in data['datas']['xscjcx']['rows']])
lesson_score = pd.DataFrame([rows['XSZCJMC'] for rows in data['datas']['xscjcx']['rows']])
lesson_kind = pd.DataFrame([rows['KCLBDM_DISPLAY'] for rows in data['datas']['xscjcx']['rows']])
study_kind = pd.DataFrame([rows['CXCKDM_DISPLAY'] for rows in data['datas']['xscjcx']['rows']])

pd = pd.concat([lesson_college, lesson_name, lesson_MAIN_score, lesson_level, lesson_score, lesson_kind, study_kind], axis=1)
pd.to_excel('data.xlsx', sheet_name='Sheet1', index=False, header=None)
