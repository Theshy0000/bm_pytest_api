'''
主业务流程：
    1.获取运单号单
    2.录单
    3.获取调度单号
    4.创建调度单选择下游承运商（回单付）
    5.派单
    6.发车
    7.到达
    9.回单上传
    10.回单确认
    11.生成回单付支付订单
    12.获取支付订单信息
    13.线上支付到卡
    14.支付审核信息查询
    15.支付审批通过
    16.新增上游账单
    17.确认上游账单
    19.切换班博系统认领流水
    20.流水核销上游账单
    21.生成下游账单
    22.确认下游账单
    23.生成尾款
    24.尾款支付
'''
import random
import allure
import pytest

from data.raw_parameter import *
from tool.requests_ import Requests
from tool.parameter_setting import ParameterSetting

parameter = ParameterSetting()
rv = parameter.rv  # 存储接口返回参数，接口依赖时读取
requests = Requests()

@allure.description("主流程")
@pytest.mark.waybill
class TestMainProcess:
    @allure.description("获取运单号")
    def test_get_waybill_no(self):
        result = requests.get('/waybill/generateWaybillNo').json()
        #参数提取
        parameter.update_rv({'waybillNo': result['content']})

        assert result['code'] == 0

    @allure.description("创建运单")
    def test_create_waybill(self):
        #依赖表达式
        replace_expression = {'waybillNo': rv['waybillNo']}
        #方法参数替换
        parameter.parameters_depend(upstream_create_waybill_data, replace_expression, rv)
        #字典原始参数替换
        upstream_create_waybill_data['customerOrderNo'] = f'ce{random.randint(100, 999)}'
        result = requests.post('/waybill/createWaybill', upstream_create_waybill_data).json()

        assert result['code'] == 1
