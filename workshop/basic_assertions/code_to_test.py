# -*- coding: utf-8 -*-
from random import choice


class Person(object):
    def __init__(self, name):
        self.name = name


class MyFantasticClass(object):
    def __init__(self, index):
        self.index = index
        self.names_list = ["Name1", "Name2", "nAmE3"]

    def get_name_by_index(self):
        return self.names_list[self.index]

    def get_person(self):
        return Person(self.get_name_by_index())

    def get_random_name(self):
        return choice(self.names_list)
