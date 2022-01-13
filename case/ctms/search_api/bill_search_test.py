'''账单搜索接口'''
import allure
import pytest
import time
from tool.log import logger
from tool.requests_ import Requests
from tool.yaml_ import YamlUsage

request = Requests()
yml = YamlUsage(r'F:\bm_api\data\bill_search_data.yaml')
data_yml = yml.read_yaml()


@allure.description('账单搜索')
@pytest.mark.parametrize('data', data_yml, ids=[  # 给每组参数都给与意思
    '账单年月搜索',
    '项目搜索',
    '状态搜索'
])
def test_bill_search(data):
    time.sleep(1)  # 搜索接口太频繁会访问失败
    result = request.post('/bill/getBillCommonList', data=data).json()
    logger.info(f'接口地址:/bill/getBillCommonList ,请求参数:{data},返回结果:{result}')
    assert result['code'] == 0
