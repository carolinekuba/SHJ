#encoding:utf-8
import requests

import Url as Url

def getJwt():
    headers = {"Content-Type":"application/json",
                "language": "zh_CN",
                "Accept": "*/*"}
    data = {"phone": "18328412017",
            "password": "E10ADC3949BA59ABBE56E057F20F883E"}
    r = requests.post(Url.commonUrl + Url.loginUrl, json=data, headers=headers)
    headers['Authorization'] = r.json()['data']['jwt']
    return headers

