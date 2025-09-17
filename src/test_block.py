import unittest
from block import *


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

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("####### Not heading"), BlockType.PARAGRAPH)

    def test_code(self):
        self.assertEqual(block_to_block_type("```code block```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```print('hi')```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("``code block``"), BlockType.PARAGRAPH)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(">Another quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(" > Not a quote"), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("123. Another item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1 First item"), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- List item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("* List item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("+ List item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("List item"), BlockType.PARAGRAPH)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Just a paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
    
class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraph(self):
        md = "This is a paragraph."
        node = markdown_to_html_node(md)
        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children[0].tag, "p")

    def test_heading(self):
        md = "# Heading 1"
        node = markdown_to_html_node(md)
        self.assertEqual(node.children[0].tag, "h1")

    def test_code_block(self):
        md = "```print('hello')```"
        node = markdown_to_html_node(md)
        self.assertEqual(node.children[0].tag, "pre")
        self.assertEqual(node.children[0].children[0].tag, "code")

    def test_quote(self):
        md = "> This is a quote\n> spanning two lines."
        node = markdown_to_html_node(md)
        self.assertEqual(node.children[0].tag, "blockquote")

    def test_ordered_list(self):
        md = "1. First\n2. Second"
        node = markdown_to_html_node(md)
        self.assertEqual(node.children[0].tag, "ol")
        self.assertEqual(node.children[0].children[0].tag, "li")

    def test_unordered_list(self):
        md = "- Item 1\n- Item 2"
        node = markdown_to_html_node(md)
        self.assertEqual(node.children[0].tag, "ul")
        self.assertEqual(node.children[0].children[0].tag, "li")

    def test_multiple_blocks(self):
        md = "# Heading\n\nParagraph\n\n- List"
        node = markdown_to_html_node(md)
        self.assertEqual(node.children[0].tag, "h1")
        self.assertEqual(node.children[1].tag, "p")
        self.assertEqual(node.children[2].tag, "ul")
if __name__ == "__main__":
    unittest.main()