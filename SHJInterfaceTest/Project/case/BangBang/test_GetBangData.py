# coding:utf-8
import requests
import unittest

import sys
sys.path.append("/Users/mac/venv/SHJInterfaceTest/Project/case")
import Url as Url

sys.path.append("/Users/mac/venv/SHJInterfaceTest/Project")
import run_all_case as run
headers = run.headers

class JwtClass(unittest.TestCase):
    def setUp(self):
        pass

    def testGetBangTimeData(self):
        par = {'areaId':'641020100'}
        self.r = requests.get(Url.commonUrl+Url.getBangDataUrl,params=par,headers=headers)
        m = self.r.json()['code']
        print m
        self.assertEqual(u'200',m)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

