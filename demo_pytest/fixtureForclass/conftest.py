# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 15:02
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : conftest.py.py
# @Software: PyCharm
import pytest
import uuid

@pytest.fixture()
def declass():
    print("declass:"+str(uuid.uuid4()))
    return "declass"

@pytest.fixture()
def declass2():
    print("declass2:"+str(uuid.uuid4()))
    return "declass2"