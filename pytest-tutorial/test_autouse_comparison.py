import unittest

import pytest


class TestUnitTest(unittest.TestCase):
    def setUp(self):
        self.foo = 42

    def test_foo(self):
        self.assertEqual(self.foo, 42)


class TestPyTest:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.foo = 42

    def test_foo(self):
        assert self.foo == 42
