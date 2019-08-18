# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 13:47
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : test_ffactory.py
# @Software: PyCharm
import pytest

@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {
        "name": name,
        "orders": []
        }
    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
    print(customer_1)
    print(customer_2)
    print(customer_3)