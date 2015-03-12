# -*- coding: utf-8 -*-
import unittest
from mock import MagicMock
from code_to_test import MyFantasticClass
"""
1. Create TestCase for MyFantasticClass tests
2. Add lines which will execute our tests
3. Create method with creating mock and object to test -> This method should be executed before every test
4. Create tests method for testing MyFantasticCLass:
    4.1 Check if check_attribute method returns appropriate value if attribute is True
    4.2 Check if check_attribute method returns appropriate value if attribute is False
    4.3 Check if check_attribute method raises exception if attribute is integer

    4.4 Check if do_nothing_or_raise_exception really do nothing when bool_value is False
        Remember you need to be sure that appropriate method of some_object was executed!
    4.5 Check if do nothing_or_raise_exception raises exception what bool_value is True

    4.6 Check if do_nothing_few_times executed do_usually_nothing some_object method "few" times and every execution has correct arguments
    4.7 Check if do_nothing_few_times wasn't executed when amount argument was 0

    4.8 Check if sum_numbers method returns 6

NOTE: You can't execute MyFantasticHelper object methods directly! You need to mock this object and code its behaviour!
"""
