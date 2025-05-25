import unittest
from core.fps_reducer import reduce_fps
import os

class TestFPSReducer(unittest.TestCase):
    def test_invalid_file(self):
        with self.assertRaises(Exception):
            reduce_fps("nonexistent.mp4", "out.mp4", 10)

# You can add real test videos later for more realistic tests
