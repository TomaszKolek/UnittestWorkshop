# -*- coding: utf-8 -*-
import random
import datetime


class MyFantasticHelper(object):

    @property
    def my_attr(self):
        return random.randrange(10)


class MyFantasticClass(object):
    def __init__(self):
        self.some_object = MyFantasticHelper()

    def do_something(self):
        random_int = self.some_object.my_attr
        if random_int == 1:
            return "1: a"
        elif random_int == 4:
            return "4: d"
        else:
            return "Some strange number"

    def do_something_by_date(self):
        date = datetime.datetime.now()
        if date.day == 10:
            return "Today is 10"
        elif date.day == 20:
            return "Today is 20"
        else:
            return "LOL I DON'T KNOW"
