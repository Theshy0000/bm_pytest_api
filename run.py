import pytest
import os
import shutil
if __name__ == '__main__':
    try:
        # 删除之前的文件夹
        shutil.rmtree("report/allure_raw")
    except:
        print('之前未生成报告原文件')
    pytest.main([])
    #编译报告原文件并启动报告服务
    os.system('allure serve report/allure_raw')

