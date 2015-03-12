# -*- coding: utf-8 -*-
import unittest
from code_to_test import MyFantasticClass, Person


class TestMyFantasticClass(ChangeMe):
    # WHAT CLASS SHOULD TEST INHERIT FROM?

    def change_me(self):
        # WHAT IS NAME OF METHOD EXECUTED BEFORE EVERY TEST?
        # WHY WE SHOULD USE IT INSTEAD OF METHOD EXECUTED ONCE BEFORE ALL TESTS?
        self.my_fantastic_object = MyFantasticClass(index=0)

    def check_if_index_was_correctly_set(self):
        # IS EVERYTHING OK WITH TEST METHOD NAME?
        # ADD TESTS HERE -> CHECK IF 0 WAS SET AS INDEX
        pass

    def test_check_if_correct_name_will_be_returned_by_get_name_by_index_method(self):
        # ADD TESTS HERE -> CHECK IF RETURNED NAME WILL BE CORRECT ELEMENT FROM names_list
        pass

    def test_check_if_get_name_by_index_method_raises_error_when_index_is_not_correct(self):
        index = 3
        # ADD TESTS HERE -> CHECK IF METHOD RAISES INDEX ERROR

    def test_check_if_get_random_name_returns_correct_name(self):
        random_name = self.my_fantastic_object.get_random_name()
        # ADD TESTS HERE -> CHECK IF RETURNED NAME IS ONE FROM THE LIST

    def test_check_if_get_person_returns_person_class_object(self):
        potential_person_object = self.my_fantastic_object.get_person()
        # ADD TESTS HERE -> CHECK IF RETURNED OBJECT IS PERSON CLASS OBJECT
        # LOOK AT THE CODE -> WHY THIS TEST IS NOT GOOD ONE?


if __name__ == "__main__":
    pass
    # WRITE TEST EXECUTOR
