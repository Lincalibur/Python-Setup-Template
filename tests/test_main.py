# tests/test_main.py
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))

from main import main

def test_main_output():
    expected_output = [
        "Hello, World!",
        "This is a placeholder script for the Python setup template repository.",
        "Feel free to replace this with your own code!"
    ]
    output = main()
    assert output == expected_output
