# tests/conftest.py
import sys
from pathlib import Path

# Add the src directory to the Python path for all tests
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
