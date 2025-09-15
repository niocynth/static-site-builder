import unittest

from inline import *
from textnode import *

class TestTextNode(unittest.TestCase):
    # split_nodes_delimited tests
    def test_split_nodes_delimited_code_middle(self):
        node = TextNode("This is a `code block` with text either side.", TextType.TEXT)
        result = split_nodes_delimited([node], "`", TextType.CODE)
        validation = [TextNode("This is a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" with text either side.", TextType.TEXT)]
        print("\nsplit_node_delimited_code_middle")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)
    
    def test_split_nodes_delimited_code_end(self):
        node = TextNode("This is just a `code block`", TextType.TEXT)
        result = split_nodes_delimited([node], "`", TextType.CODE)
        validation = [TextNode("This is just a ", TextType.TEXT), TextNode("code block", TextType.CODE)]
        print("\nsplit_node_delimited_code_end")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_split_nodes_delimited_bold_middle(self):
        node = TextNode("This is **bold text** in a sentence.", TextType.TEXT)
        result = split_nodes_delimited([node], "**", TextType.BOLD)
        validation = [TextNode("This is ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" in a sentence.", TextType.TEXT)]
        print("\nsplit_node_delimited_bold_middle")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_split_nodes_delimited_mixed(self):
        node = TextNode("This sentence has **bold text** and a `code block` in it.", TextType.TEXT)
        result1 = split_nodes_delimited([node], "**", TextType.BOLD)
        validation1 = [TextNode("This sentence has ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" and a `code block` in it.", TextType.TEXT)]
        result2 = split_nodes_delimited([node], "`", TextType.CODE)
        validation2 = [TextNode("This sentence has **bold text** and a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" in it.", TextType.TEXT)]
        print("\nsplit_node_delimited_mixed")
        print(f"Result 1: {result1}")
        print(f"Validation 1: {validation1}")
        print(f"Result 2: {result2}")
        print(f"Validation 2: {validation2}")
        self.assertEqual(validation1, result1)
        self.assertEqual(validation2, result2)
        self.assertNotEqual(validation1, result2)

    def test_split_nodes_delimited_missing_delimiter(self):
        node = TextNode("This is **bold text in a sentence.", TextType.TEXT)
        print("\nsplit_node_delimited_missing_delimiter")
        print("Exception: Invalid Markdown syntax")
        with self.assertRaisesRegex(Exception, "Invalid Markdown syntax"):
            split_nodes_delimited([node], "**", TextType.BOLD)

    def test_split_nodes_delimited_multiple_input(self):
        nodes = [TextNode("This is **bold text** in a sentence.", TextType.TEXT), TextNode("This sentence has **bold text** and a `code block` in it.", TextType.TEXT)]
        result = split_nodes_delimited(nodes, "**", TextType.BOLD)
        validation = [TextNode("This is ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" in a sentence.", TextType.TEXT),TextNode("This sentence has ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" and a `code block` in it.", TextType.TEXT)]
        print("\nsplit_node_delimited_bold_multiple_input")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_split_nodes_delimited_double(self):
        node = TextNode("This sentence has **bold text** and a `code block` in it.", TextType.TEXT)
        first = split_nodes_delimited([node], "**", TextType.BOLD)
        result = split_nodes_delimited(first, "`", TextType.CODE)
        validation = [TextNode("This sentence has ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" and a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" in it.", TextType.TEXT)]
        print("\nsplit_node_delimited_double")
        print(f"First: {first}")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_split_nodes_delimited_italics_start(self):
        node = TextNode("_italic text_ at the start of the sentence", TextType.TEXT)
        result = split_nodes_delimited([node], "_", TextType.ITALIC)
        validation = [TextNode("italic text", TextType.ITALIC), TextNode(" at the start of the sentence", TextType.TEXT)]
        print("\nsplit_node_delimited_italics_start")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)