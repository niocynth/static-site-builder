import unittest

from main import *

class TestExtractTitle(unittest.TestCase):
    def test_title_at_start(self):
        md = "# My Title\nSome content here."
        self.assertEqual(extract_title(md), "My Title")

    def test_title_with_leading_spaces(self):
        md = "   # Leading Title\nOther text."
        self.assertEqual(extract_title(md.lstrip()), "Leading Title")

    def test_title_in_middle(self):
        md = "Intro text\n# Middle Title\nMore text."
        self.assertEqual(extract_title(md), "Middle Title")

    def test_title_with_extra_hashes(self):
        md = "# Title #\nContent"
        self.assertEqual(extract_title(md), "Title #")

    def test_no_title_raises(self):
        md = "No title here\nJust text"
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()