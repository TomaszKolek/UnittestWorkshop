# -*- coding: utf-8 -*-
import unittest
from code_to_test import MyFantasticClass, Person


class TestMyFantasticClass(unittest.TestCase):

    def setUp(self):
        # WE NEED TO CREATE "FRESH" OBJECT BEFORE EVERY TEST TO BE SURE THAT WE ARE OPERATING ON NOT MODIFIED OBJECT
        self.index = 0
        self.my_fantastic_object = MyFantasticClass(index=self.index)

    def test_check_if_index_was_correctly_set(self):
        self.assertEqual(self.my_fantastic_object.index, 0)

    def test_check_if_correct_name_will_be_returned_by_get_name_by_index_method(self):
        self.assertEqual(self.my_fantastic_object.get_name_by_index(), self.my_fantastic_object.names_list[self.index])

    def test_check_if_get_name_by_index_method_raises_error_when_index_is_not_correct(self):
        index = 3
        self.my_fantastic_object.index = index
        self.assertRaises(IndexError, self.my_fantastic_object.get_name_by_index)
        with self.assertRaises(IndexError):
            self.my_fantastic_object.get_name_by_index()

    def test_check_if_get_random_name_returns_correct_name(self):
        random_name = self.my_fantastic_object.get_random_name()
        self.assertIn(random_name, self.my_fantastic_object.names_list)

    def test_check_if_get_person_returns_person_class_object(self):
        potential_person_object = self.my_fantastic_object.get_person()
        self.assertIsInstance(potential_person_object, Person)
        # NO WE SHOULD TEST SEPARATED FUNCTIONALITY HERE WE EXECUTE TESTING METHOD AND GET_NAME_BY_INDEX


if __name__ == "__main__":
    pass
    # WRITE TEST EXECUTOR
