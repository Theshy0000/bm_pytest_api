import pytest
from data.config_data import *


@pytest.fixture()
def login():
    print("登录成功！")


@pytest.fixture()
def global_variable():
    '''全局变量配置'''
    variable = {
        'test_ip': TEST_IP,
        'downstream_token': DOWNSTREAM_TOKEN,
        'upstream_token': UPSTREAM_TOKEN
    }
    return variable
