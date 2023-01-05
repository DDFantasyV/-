import requests
import json
import pandas as pd

url = 'https://jwgl.wvpn.hrbeu.edu.cn/jwapp/sys/cjcx/modules/cjcx/xscjcx.do'
cookies = {'cookie_name': '请换成自己的cookie！'}

response = requests.get(url, cookies=cookies)
data = json.loads(response.text)

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
