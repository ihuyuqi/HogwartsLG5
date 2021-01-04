# -*- coding: utf-8 -*-
# @Author : feier
# @File : conftest.py
import pytest
import yaml

# from test_pytest.pythoncode.calculator import Calculator
import os

# 通过 os.path.dirname 获取当前文件所在目录的路径
from test_pytest.pythoncode.calculator import Calculator

yaml_file_path = os.path.dirname(__file__) + "/data.yml"

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    print(datas)
    # 获取文件中key为datas的数据
    add_datas = datas["datas"]
    # 获取文件中key为myids的数据
    add_ids = datas["myids"]
    # 获取文件中key为datas_sub的数据
    sub_datas = datas["datas_sub"]
    # 获取文件中key为myids_sub的数据
    sub_ids = datas["myids_sub"]
    # 获取文件中key为datas_mul的数据
    mul_datas = datas["datas_mul"]
    # 获取文件中key为myids_mul的数据
    mul_ids = datas["myids_mul"]
    # 获取文件中key为datas_div的数据
    div_datas = datas["datas_div"]
    # 获取文件中key为myids_mul的数据
    div_ids = datas["myids_div"]


@pytest.fixture(params=add_datas, ids=add_ids, scope="module")
def get_datas(request):
    print("\n开始计算")
    data = request.param
    print(f"加法request.param的测试数据是：{data}")
    yield data
    print("\n结束计算")


@pytest.fixture(params=mul_datas, ids=mul_ids, scope="module")
def get_muldatas(request):
    print("\n开始计算")
    data = request.param
    print(f"乘法 request.param的测试数据是：{data}")
    yield data
    print("\n结束计算")


@pytest.fixture(params=sub_datas, ids=sub_ids, scope="module")
def get_subdatas(request):
    print("\n开始计算")
    data = request.param
    print(f"减法 request.param的测试数据是：{data}")
    yield data
    print("\n结束计算")


@pytest.fixture(params=div_datas, ids=div_ids, scope="module")
def get_divdatas(request):
    print("\n开始计算")
    data = request.param
    print(f"除法 request.param的测试数据是：{data}")
    yield data
    print("\n结束计算")


# @pytest.fixture(scope="session")
# def connectDB():
#     print("连接数据库操作")
#     yield
#     print("断开数据库连接")

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc
