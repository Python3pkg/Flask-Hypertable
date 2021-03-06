#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `flask_hypertable` module."""



from .. import flask_hypertable

from . import unittest


class Flask_hypertableTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def test_something_docstring(self):
        """Here is a sample test with a docstring. Hey."""
        self.assertTrue(True)

    def tearDown(self):
        pass


def suite():
    from .helpers import setup_path
    setup_path()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Flask_hypertableTestCase))
    return suite