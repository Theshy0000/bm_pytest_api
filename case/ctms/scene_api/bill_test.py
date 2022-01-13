'''
    账单相关流程：
    1.新增账单
    2.删除账单
'''

import random

import allure

from data.raw_parameter import *
from tool.requests_ import Requests
from tool.parameter_setting import ParameterSetting

parameter = ParameterSetting()
rv = parameter.rv  # 存储接口返回参数，接口依赖时读取
requests = Requests()
@allure.description("账单操作")
class TestBill:
    @allure.description("创建账单")
    def test_create_bill(self,global_variable):
        print(f'使用下全局变量{global_variable["test_ip"]}')
        result=requests.post('/bill/createCommonBill',create_bill_data).json()
        print(result)
        parameter.update_rv({'id':result['content']['id']})

    @allure.description("删除账单")
    def test_delete_bill(self):
        replace_expression={'id':rv['id']}
        parameter.parameters_depend(delete_bill_data,replace_expression,rv)
        result=requests.post('/bill/deleteBillCommon',delete_bill_data)
        print(result.json())