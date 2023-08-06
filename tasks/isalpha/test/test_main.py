import unittest
from main import is_alpha_or_what

class TestIsAlphaOrWhat(unittest.TestCase):

    def test_alphanumberic(self):
        result = is_alpha_or_what('ab123')
        self.assertEqual(result['alphanumeric'], True)
        self.assertEqual(result['alphabetic'], True)
        self.assertEqual(result['digit'], True)
        self.assertEqual(result['lower'], True)
        self.assertEqual(result['upper'], False)

    def test_bad_word_with_digits(self):
        result = is_alpha_or_what('#%@$#42**!')
        self.assertEqual(result['alphanumeric'], True)
        self.assertEqual(result['alphabetic'], False)
        self.assertEqual(result['digit'], True)
        self.assertEqual(result['lower'], False)
        self.assertEqual(result['upper'], False)


