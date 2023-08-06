import unittest
from main import count_substring

class TestCountSubstring(unittest.TestCase):

    def test_count_one(self):
        s = "foobar"
        ss = "foo"
        result = count_substring(s, ss)
        self.assertEqual(result, 1)
        # Confirm result using built-in count() function
        self.assertEqual(result, s.count(ss))

    def test_count_two(self):
        s = "foobar fookabane"
        ss = "foo"
        result = count_substring(s, ss)
        # Confirm result using built-in count() function
        self.assertEqual(result, s.count(ss))

    def test_overlapping(self):
        # test case with overlapping occurrences
        self.assertEqual(count_substring("aaaaaa", "aa"), 5)

    


