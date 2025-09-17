import unittest
from block import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_single_block(self):
        md = "This is a single block."
        self.assertEqual(markdown_to_blocks(md), ["This is a single block."])

    def test_multiple_blocks(self):
        md = "Block one.\n\nBlock two.\n\nBlock three."
        self.assertEqual(
            markdown_to_blocks(md),
            ["Block one.", "Block two.", "Block three."]
        )

    def test_blocks_with_whitespace(self):
        md = "  Block one.  \n\n   Block two.   \n\nBlock three.   "
        self.assertEqual(
            markdown_to_blocks(md),
            ["Block one.", "Block two.", "Block three."]
        )

    def test_blocks_with_extra_linebreaks(self):
        md = "Block one.\n\n\n\nBlock two."
        self.assertEqual(
            markdown_to_blocks(md),
            ["Block one.", "Block two."]
        )

    def test_blocks_with_only_whitespace_between(self):
        md = "Block one.\n\n   \n\nBlock two."
        self.assertEqual(
            markdown_to_blocks(md),
            ["Block one.", "Block two."]
        )

    def test_consecutive_double_linebreaks(self):
        md = "Block one.\n\n\n\n\n\nBlock two."
        self.assertEqual(
            markdown_to_blocks(md),
            ["Block one.", "Block two."]
        )

    def test_block_with_empty_blocks(self):
        md = "Block one.\n\n\n\n\n\n\n\nBlock two."
        self.assertEqual(
            markdown_to_blocks(md),
            ["Block one.", "Block two."]
        )

if __name__ == "__main__":
    unittest.main()