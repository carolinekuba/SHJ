#coding: utf-8
import requests
import unittest

import sys
sys.path.append("/Users/mac/venv/SHJInterfaceTest/Project/case")
import Login as Login
import Url as Url

sys.path.append("/Users/mac/venv/SHJInterfaceTest/Project")
import run_all_case as run
headers = run.headers

class JwtClass(unittest.TestCase):
    def setUp(self):
        pass

    def testGetBangOrderList(self):
        u'获取帮帮送订单列表用例'
        payload = {"start":"0",
             "limit":"5",
             "keyWords":"18328412017",
             "areaId":"64",
             "status":"S_CANCLE"}
        self.r = requests.post(Url.commonUrl+Url.getBangOrderListUrl, json=payload, headers=headers)
        m = self.r.json()['code']
        print m
        self.assertEqual(u'200', m)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

