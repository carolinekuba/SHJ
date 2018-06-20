#coding:utf-8
import unittest
import os
import HTMLTestRunner

import case.Login as Login
headers = Login.getJwt()
print headers

def all_case():
    #待执行用例的目录
    case_path = os.path.join(os.getcwd(), "case")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)

    testcase.addTests(discover)
    print testcase
    return testcase

if __name__ == "__main__":

    #返回实例
    #runner = unittest.TextTestRunner()
    report_path = "//Users//mac//venv//SHJInterfaceTest//Project//test_report//result.html"
    fp = file(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Report中文测试', description='This is my test report')

    #run所有的用例
    runner.run(all_case())
    fp.close()

