#encoding:utf-8
import requests
import unittest

import sys
sys.path.append("..")
import Login as Login
import Url as Url

sys.path.append("/Users/mac/venv/SHJInterfaceTest/Project")
import run_all_case as run
headers = run.headers
class GetLunch(unittest.TestCase):
    def setUp(self):
        pass

    #获取快捷午餐订单列表
    def test_getLunch(self):
        self.par = {"start": "0", "limit": "4", "sortType": "asc", "status": "S_COMPLETE"}
        self.r = requests.get(Url.commonUrl+Url.getLunchOrderListUrl, params=self.par,
                              headers=headers)
        m = self.r.json()['code']
        print m
        self.assertEqual(u'200', m)

    #获取商城折扣码统计
    def test_getMallDiscountCode(self):
        self.par = {"code":"000","orderType":"","start":"0","limit":"4","beginTime":"1525881600","endTime":"1525953600"}
        self.r = requests.get(Url.commonUrl+Url.getMallDiscountCodeUrl,params=self.par,headers=headers)
        m = self.r.json()['code']
        self.assertEqual(u'200',m)

    #获取快捷午餐订单详情---->不可用
    '''def test_getLunchDetail(self):
        self.par = {"shopId":"42387967"}
        self.r = requests.get(Url.commonUrl+Url.getLunchOrderDetailUrl,params=self.par,headers=headers)
        print self.r

    #添加到收藏----> 不可用
    def test_addToCart(self):
        self.data = {"mallSaleChannelId":"20200002"}
        self.r = requests.post(Url.commonUrl+Url.addToFavoritesUrl,json=self.data,headers=headers)
        print self.r'''

    #获取收藏列表接口
    def test_getFavoritesUrl(self):
        self.par = {"mallSaleChannelId":"20200002"}
        self.r = requests.get(Url.commonUrl+Url.getFavoritesUrl,params=self.par,headers=headers)
        m = self.r.json()['code']
        self.assertEqual(u'200',m)

    ''''#获取商品详情
    def test_getGoodsDetailUrl(self):
        self.r = requests.get(Url.commonUrl+Url.getGoodsDetailUrl,headers=headers)
        m = self.r.json()['code']
        self.assertEqual(u'200',m)'''

    #获取商城和快捷午餐订单配送汇总
    def test_getOrderTotal(self):
        self.data = {"start":"1","limit":"4","status":"S_COMPLETE","channelTypeList":"B_NZ_LOCAL"}
        self.r = requests.post(Url.commonUrl+Url.getOrderTotalUrl,json=self.data,headers=headers)
        m = self.r.json()['code']
        self.assertEqual(u'200',m)

    # 本地商城，邮购，快捷午餐业务实时运营数据
    def test_getTimeOperatingData(self):
        self.par = {"areaId":"641020100","mallShopType":"B_NZ_LOCAL"}
        self.r = requests.get(Url.commonUrl+Url.getTimeOperatingDataUrl,params=self.par,headers=headers)
        m = self.r.json()['code']
        self.assertEqual(u'200',m)

    #获取活动列表---->400
    def test_getActivityList(self):
        self.par = {"shopId":"42387967"}
        self.r = requests.get(Url.commonUrl+Url.getActivityListUrl,params=self.par,headers=headers)
        m = self.r.json()['code']
        self.assertEqual(u'200',m)

    #获取本地商城，邮购，快捷午餐数据统计--->400
    def test_getDataStatistics(self):
        self.data = {"areaIdList":"641020100,642050700"}
        self.r = requests.post(Url.commonUrl+Url.getDataStatisticsUrl,json=self.data,headers=headers)
        m = self.r.json()['code']
        self.assertEqual(u'200',m)

    #提交快捷午餐订单
    def test_submitLunchOrder(self):
        self.r = requests.get(Url.commonUrl+Url.submitLunchOrderUrl,headers=headers)
        m = self.r.json()
        print m

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
