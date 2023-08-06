import unittest
import sys
from io import StringIO
import re

from main import get_substrings

class TestGetSubstrings(unittest.TestCase):

    def test_untilities(self):
        """
        Test
        - lambda that generte condition
        - redirection from stdout to StringIO buffer
        """
        original_stdout = sys.stdout
        vowels = ['a', 'e', 'i', 'o', 'u']

        buffer = StringIO()
        sys.stdout = buffer

        ch = 'a'
        is_vowel = lambda char: char in vowels
        print("vowel") if is_vowel(ch) else print("not vowel")
        self.assertEqual(buffer.getvalue().strip(), "vowel")

        buffer.flush()
        sys.stdout = original_stdout

        buffer = StringIO()
        sys.stdout = buffer

        ch = 'b'
        print("vowel") if is_vowel(ch) else print("not vowel")
        self.assertEqual(buffer.getvalue().strip(), "not vowel")

    def test_starts_with_vowel(self):
        string = 'banana'
        result = get_substrings(string, 'v')
        self.assertEqual(result, {'a': 3, 'an': 2, 'ana': 2, 'anan': 1, 'anana': 1})
        self.assertEqual(sum(result.values()), 9)

    def test_starts_with_consonant(self):
        string = 'banana'
        result = get_substrings(string, 'c')
        self.assertEqual(result, {'b': 1, 'ba': 1, 'ban': 1, 'bana': 1, 'banan': 1, 'banana': 1, 'n': 2, 'na': 2, 'nan': 1, 'nana': 1})
        self.assertEqual(sum(result.values()), 12)


    def test_arg_error(self):
        """
        Test the error message in the console if command line arguments are missing. 
        Redirect error in the console to a StringIO buffer and capture the output.

        Initially, sys.stdout represents the standard output, which points to the console.
        Any print statements will display their output on the console.

        sys.stdout = stdout_buffer changes where the standard output goes. 
        Instead of pointing to the console, it now points to the StringIO buffer.

        After the redirection, any print statement will write its output to the stdout_buffer instead of displaying it in the console. 
        """

        expected_error_message = """
            Usage: python <script.py> <string> <starts_with>. 
            Use 'c' (consonant) and 'v' (vowel) for <starts_with>.
            Example: python script.py banana c
        """.strip()

        stdout_buffer = StringIO()
        sys.stdout = stdout_buffer

        with self.assertRaises(SystemExit) as context:
            get_substrings()

        # Capture the printed output from the StringIO buffer
        printed_output = stdout_buffer.getvalue().strip()

        self.assertEqual(context.exception.code, 1)

        # To handle variation in spacing, use \s* in place of the space characters.
        # Regex will match any number of whitespace characters (including zero) between words
        regex_pattern = re.escape(expected_error_message).replace(r'\ ', r'\s*')
        match = re.search(regex_pattern, printed_output)
        self.assertIsNotNone(match)