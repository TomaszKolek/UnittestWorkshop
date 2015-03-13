# -*- coding: utf-8 -*-
from checker_decorator import checker


class MyFantasticHelper(object):
    #@checker
    def do_usually_nothing(self, bool_value=False):
        if bool_value is True:
            raise Exception("Ops bool value is True")

    #@checker
    def do_something(self, attr):
        if isinstance(attr, int):
            raise Exception("We don't want get int!")
        elif attr is True:
            return "Attribute is True"
        elif attr is False:
            return "Attribute is False"
        else:
            return attr

    #@checker
    def get_number(self, number):
        return number


class MyFantasticClass(object):
    def __init__(self):
        self.some_object = MyFantasticHelper()

    def check_attribute(self, attribute):
        return self.some_object.do_something(attribute)

    def do_nothing_or_raise_exception(self, bool_value):
        self.some_object.do_usually_nothing(bool_value)

    def do_nothing_few_times(self, amount):
        for i in range(amount):
            self.some_object.do_usually_nothing(amount)

    def sum_numbers(self):
        numbers_list = [1, 2, 3]
        solution = 0
        for number in numbers_list:
            solution += self.some_object.get_number(number)
        return solution
