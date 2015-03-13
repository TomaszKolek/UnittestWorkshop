# -*- coding: utf-8 -*-
import unittest
from mock import patch
from code_to_test import MyFantasticClass
"""
1. Create TestCase for MyFantasticClass tests
2. Add lines which will execute our tests
3. Create tests method for testing MyFantasticCLass:
    3.1 Check if instance fields are correctly created. Remember to do not create MyFantasticHelper, just mock it
    3.2 Check if do_something methods returns correctly value for 1, 4 and some another random_int
    3.3 Check if do_something_by_date method returns correctly value for date where day is 10, 20 or another.
    datetime.now function should return MagicMock object with appropriate attributes

    NOTE: You can't execute MyFantasticHelper object methods directly! You need to mock this object and code its behaviour!
"""