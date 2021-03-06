# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 23:26
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : userfc.py
# @Software: PyCharm
import factory
import factory.fuzzy
from demo_factory_boy.fbobject.user import User
from demo_factory_boy.fbobject.school import School
from demo_factory_boy.fbobject.home import Home
from demo_factory_boy.fbprivader.numpv import NumProvider

factory.Faker.add_provider(NumProvider)  #添加自定义的NumProvider

class HomeFactory(factory.Factory):
    class Meta:
        model = Home

    address = factory.sequence(lambda n: 'address%04d' % n)#factory.sequence
    name=["hhh",2]

class SchoolFactory(factory.Factory):
    class Meta:
        model = School

    schoolName = factory.sequence(lambda n: 'school%04d' % n)#factory.sequence
    home=factory.List(factory.build_batch(HomeFactory, 4))


class UserFactory(factory.Factory):
    class Meta:
        model = User

    name = factory.Faker("name", locale="zh_CN")#factory.Faker
    num = factory.Faker("num")
    #age = factory.fuzzy.FuzzyInteger(42)#factory.fuzzy.FuzzyInteger
    age = factory.Faker("random_int",min=18, max=30, step=1)
    city = factory.Faker("address", locale="zh_CN")
    phone = factory.fuzzy.FuzzyText("138", 7, "1", "1234567890")#factory.fuzzy.FuzzyText
    school = factory.SubFactory(SchoolFactory)#factory.SubFactory

    #info=factory.List([SchoolFactory])
    info =factory.List(factory.build_batch(SchoolFactory, 4))
    #dictmap=factory.Dict([("one",SchoolFactory),("two",SchoolFactory)])
    dictmap = factory.Dict({"one":SchoolFactory, "two":SchoolFactory})
    #dictmap = factory.Dict(dict(one=1, two=2))

    class Params:
        shipped = factory.Trait(
            name=None
        )
