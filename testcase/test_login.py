import unittest
from unittestreport import ddt,list_data
from common.handel_excel import HandleExel
from login_func import login_check
from  common.handler_log import my_log
from common.hande_path import DATA_DIR
import os
@ddt
class TestLogin(unittest.TestCase):
    excel = HandleExel(os.path.join(DATA_DIR,"cases.xlsx"),"login")
    cases = excel.read_data()

    @list_data(cases)
    def test_login(self,item):
        #第一步:准备测试数据
        expected = eval(item['expected'])
        params = eval(item['data'])
        row = item['case_id'] + 1
        #第二步:调用功能函数(接口)进行测试,获取结果
        res = login_check(**params)
        #第三步:断言--->测试结果回写，日志输出
        try:
            self.assertEqual(expected,res)
        except AssertionError as e:
            self.excel.write_data(row=row,column=5,value='不通过')
            my_log.error('用例---{}---执行失败'.format(item['title']))
            # my_log.error(e)
            #记录详细的错误信息到日志
            my_log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=5, value='通过')
            my_log.info('用例---{}---执行成功'.format(item['title']))
