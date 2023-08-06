#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Usage: $0 <directory_name>"
  exit 1
fi

directory_name="$1"

# Create directories
mkdir -p "$directory_name"/test

# Create main.py file
echo "def hello_world():" > "$directory_name"/main.py
echo "    return \"Hello, World!\"" >> "$directory_name"/main.py

# Create test_main.py file
echo "import unittest" > "$directory_name"/test/test_main.py
echo "from main import hello_world" >> "$directory_name"/test/test_main.py
echo "" >> "$directory_name"/test/test_main.py
echo "class TestHelloWorld(unittest.TestCase):" >> "$directory_name"/test/test_main.py
echo "" >> "$directory_name"/test/test_main.py
echo "    def test_hello_world(self):" >> "$directory_name"/test/test_main.py
echo "        result = hello_world()" >> "$directory_name"/test/test_main.py
echo "        self.assertEqual(result, \"Hello, World!\")" >> "$directory_name"/test/test_main.py

# Create empty __init__.py in test folder
echo "" > $directory_name/test/__init__.py

