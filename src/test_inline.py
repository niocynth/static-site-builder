import unittest

from inline import *
from textnode import *

class TestSplitNodesDelimited(unittest.TestCase):
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

class TestExtractMarkdownImages(unittest.TestCase):
    def test_single_image(self):
        text = "![alt](http://example.com/image.png)"
        result = extract_markdown_images(text)
        print("\ntest_single_image")
        print(f"Result: {result}")
        print(f"Validation: [('alt', 'http://example.com/image.png')]")
        self.assertEqual(result, [("alt", "http://example.com/image.png")])

    def test_multiple_images(self):
        text = "![cat](cat.jpg) some text ![dog](dog.png)"
        result = extract_markdown_images(text)
        print("\ntest_multiple_images")
        print(f"Result: {result}")
        print(f"Validation: [('cat', 'cat.jpg'), ('dog', 'dog.png')]")
        self.assertEqual(result, [("cat", "cat.jpg"), ("dog", "dog.png")])

    def test_no_images(self):
        text = "This is just text without any images."
        result = extract_markdown_images(text)
        print("\ntest_no_images")
        print(f"Result: {result}")
        print(f"Validation: []")    
        self.assertEqual(result, [])

    def test_image_with_empty_alt(self):
        text = "![](emptyalt.jpg)"
        result = extract_markdown_images(text)
        print("\ntest_image_with_empty_alt")
        print(f"Result: {result}")
        print(f"Validation: [('', 'emptyalt.jpg')]")
        self.assertEqual(result, [("", "emptyalt.jpg")])

    def test_invalid_markdown(self):
        text = "[alt](notanimage.jpg) ![missingurl]()"
        result = extract_markdown_images(text)
        print("\ntest_invalid_markdown")
        print(f"Result: {result}")
        print(f"Validation: []")
        self.assertEqual(result, [])

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        text = "[Google](https://google.com)"
        result = extract_markdown_links(text)
        print("\ntest_single_link")
        print(f"Result: {result}")
        print(f"Validation: [('Google', 'https://google.com')]")
        self.assertEqual(result, [("Google", "https://google.com")])

    def test_multiple_links(self):
        text = "[One](one.com) and [Two](two.com)"
        result = extract_markdown_links(text)
        print("\ntest_multiple_links")
        print(f"Result: {result}")
        print(f"Validation: [('One', 'one.com'), ('Two', 'two.com')]")
        self.assertEqual(result, [("One", "one.com"), ("Two", "two.com")])

    def test_no_links(self):
        text = "No markdown links here!"
        result = extract_markdown_links(text)
        print("\ntest_no_links")
        print(f"Result: {result}")
        print(f"Validation: []")
        self.assertEqual(result, [])

    def test_link_with_empty_text(self):
        text = "[](/emptytext)"
        result = extract_markdown_links(text)
        print("\ntest_link_with_empty_text")
        print(f"Result: {result}")
        print(f"Validation: [('', '/emptytext')]")
        self.assertEqual(result, [("", "/emptytext")])

    def test_image_not_extracted(self):
        text = "![alt](image.png) [Link](url.com)"
        result = extract_markdown_links(text)
        print("\ntest_image_not_extracted")
        print(f"Result: {result}")
        print(f"Validation: [('Link', 'url.com')]")
        self.assertEqual(result, [("Link", "url.com")])

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image_single(self):
        node = TextNode("Here is an image ![alt](image.png) in text.", TextType.TEXT)
        result = split_nodes_image([node])
        validation = [TextNode("Here is an image ", TextType.TEXT), TextNode(None, TextType.IMAGE, {"alt": "alt", "url": "image.png"}), TextNode(" in text.", TextType.TEXT)]
        print("\ntest_split_nodes_image_single")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_split_nodes_image_multiple(self):
        node = TextNode("First ![img1](img1.png) then ![img2](img2.jpg).", TextType.TEXT)
        result = split_nodes_image([node])
        validation = [TextNode("First ", TextType.TEXT), TextNode(None, TextType.IMAGE, {"alt": "img1", "url": "img1.png"}), TextNode(" then ", TextType.TEXT), TextNode(None, TextType.IMAGE, {"alt": "img2", "url": "img2.jpg"}), TextNode(".", TextType.TEXT)]
        print("\ntest_split_nodes_image_multiple")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_split_nodes_image_none(self):
        node = TextNode("No images here, just text.", TextType.TEXT)
        result = split_nodes_image([node])
        validation = [TextNode("No images here, just text.", TextType.TEXT)]
        print("\ntest_split_nodes_image_none")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_split_nodes_image_non_text_node(self):
        node = HTMLNode("div", None, None, None)
        print("\ntest_split_nodes_image_non_text_node")
        print("TypeError: All nodes must be TextNode instances")
        with self.assertRaisesRegex(TypeError, "All nodes must be TextNode instances"):
            split_nodes_image([node])