#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""
import unittest
from unittest.mock import patch
from importlib import util
from io import StringIO
import os
import sys

proj_path = os.path.dirname(os.path.realpath(__file__ + "/.."))
if proj_path not in sys.path:
    sys.path.insert(0, proj_path)
#pylint: disable=wrong-import-position
import exam
#pylint: enable=wrong-import-position

class TestFunc(unittest.TestCase):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """


    def test_a_module(self):
        """
        Test that module and functions exist
        """
        self.assertIsNotNone(util.find_spec("exam"))
        self.assertTrue(hasattr(exam, "analyze_text"))
        self.assertTrue(hasattr(exam, "count_animals"))

    def test_b_analyze_text(self):
        """
        Test assignment 1
        """
        self.assertIsNotNone(util.find_spec("analyze_functions"))

        inp = ["s", "g", "q"]
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                exam.analyze_text()
                str_data = fake_out.getvalue().strip("\n")
                list_data = str_data.split("\n")
                self.assertEqual(float(list_data[0]), results[ind])
    
    def test_c_verify_hex(self):
        """
        Test assignment 2
        """
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)
