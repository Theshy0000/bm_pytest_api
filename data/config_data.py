#测试环境
TEST_IP = 'https://xxx.cn'
#亚申token
YA_SHENG_TOKEN = 'eyxxcFoxODdrbk1DWG85QTdxY3pwakNoUGVvVEM1Ym1BPSJ9'
#中昌token 下游
DOWNSTREAM_TOKEN='eyxPSJ9'
DOWNSTREAM_HEADERS={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'token':DOWNSTREAM_TOKEN,
    'Content-Type':'application/json'
}
#三笑token 上游
UPSTREAM_TOKEN='eyJlbmNyeXB0HFUN3d1Q5QfQ=='
UPSTREAM_HEADERS={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'token':UPSTREAM_TOKEN,
    'Content-Type':'application/json'
}
#数据库配置，使用数据库操作时使用
MYSQL_CONFIG=("101.xx.xx.xx",3306, 'root', '123456', 'drf')
