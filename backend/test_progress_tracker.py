import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))
from progress_tracker import ProgressTracker

class TestProgressTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = ProgressTracker()

    def test_set_and_get_progress(self):
        self.tracker.set_progress("12.2", "In Progress")
        self.assertEqual(self.tracker.get_progress("12.2"), "In Progress")

    def test_get_progress_not_started(self):
        self.assertEqual(self.tracker.get_progress("12.3"), "Not Started")

    def test_get_all_progress(self):
        self.tracker.set_progress("12.2", "In Progress")
        self.tracker.set_progress("12.3", "Completed")
        self.assertEqual(self.tracker.get_all_progress(), {"12.2": "In Progress", "12.3": "Completed"})

if __name__ == "__main__":
    unittest.main()
