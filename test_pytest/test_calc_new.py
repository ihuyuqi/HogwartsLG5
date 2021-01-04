# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_calc_new.py
import pytest
import yaml


class TestCalc:

    # 测试add函数
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_datas):
        result = None
        try:
            # 调用add函数,返回的结果保存在result里面
            result = get_calc.add(get_datas[0], get_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_datas[2]

    # 测试mul函数
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_muldatas):
        result = None
        try:
            # 调用mul函数,返回的结果保存在result里面
            result = get_calc.mul(get_muldatas[0], get_muldatas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_muldatas[2]

    # 测试sub函数
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_subdatas):
        result = None
        try:
            # 调用sub函数,返回的结果保存在result里面
            result = get_calc.sub(get_subdatas[0], get_subdatas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_subdatas[2]

    # 测试div函数
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_divdatas):
        result = None
        try:
            # 调用div函数,返回的结果保存在result里面
            result = get_calc.div(get_divdatas[0], get_divdatas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_divdatas[2]
