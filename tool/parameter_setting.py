class ParameterSetting(object):
    '''参数相关工具方法集合'''
    returned_value = {}


    def parameters_depend(self, request_parameter, replace_expression, rv):
        '''
        解决接口之间参数依赖替换,先找出相同的键值，然后把接口
        返回结果的值赋给替换表达式的值，最后把替换表达式的值赋值给请求参数
        :param request_parameter: 原请求参数
        :param replace_expression: 替换参数表达式 字典
        :param rv: 接口返回接口保存字典
        :return:
        '''
        key_list = self.__identical_key(request_parameter, replace_expression)
        for i in key_list:
            replace_expression[i] = rv[i]
            request_parameter[i] = replace_expression[i]
        return request_parameter

    def __identical_key(self, v1, v2):
        '''
        :param v1:  字典
        :param v2:  字典
        :return: 找出2个字典相同的键以列表格式返回键值
        '''
        s = set()
        for k in v1.keys():
            for k1 in v2.keys():
                if k == k1:
                    s.add(k)
        return list(s)

    @property
    def rv(self):
        '''解决接口之间参数依赖,读取别的接口的返回结果，使用变量名作为字典键值读取'''
        return self.returned_value

    def update_rv(self, value):
        '''
        写入返回结果，使用变量名和值的方式保存
        :param value: 字典格式数据
        '''
        for k, v in value.items():
            self.returned_value[k] = v
