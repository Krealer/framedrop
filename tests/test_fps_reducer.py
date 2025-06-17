import unittest
import os
import sys

# Ensure the project root is on the Python path when tests are run from
# outside the repository directory.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.fps_reducer import reduce_fps

class TestFPSReducer(unittest.TestCase):
    def test_invalid_file(self):
        with self.assertRaises(Exception):
            reduce_fps("nonexistent.mp4", "out.mp4", 10)

# You can add real test videos later for more realistic tests
