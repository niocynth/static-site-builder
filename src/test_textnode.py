import unittest

from textnode import *
from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is an image", TextType.IMAGE, "../images/image.png")
        node2 = TextNode("This is an image", TextType.IMAGE, "../images/image.png")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is an image", TextType.IMAGE, "../images/image.png")
        self.assertNotEqual(node, node2)
    
    def test_url_none_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_strnone_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "None")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)        

class TestTextNodeToHTMLNode(unittest.TestCase):
    # text_node_to_html_node tests
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        print("\nTextType.TEXT to html")
        print(f"TextNode: {node}")
        print(f"HTMLNode: {html_node}")
        print(f"HTML: {html_node.to_html()}")
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_text_bold(self):
        node = TextNode("This text should be bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        print("\nTextType.BOLD to html")
        print(f"TextNode: {node}")
        print(f"HTMLNode: {html_node}")
        print(f"HTML: {html_node.to_html()}")
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This text should be bold")
        self.assertEqual(html_node.to_html(), "<b>This text should be bold</b>")

    def test_text_italic(self):
        node = TextNode("This text should be italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        print("\nTextType.ITALIC to html")
        print(f"TextNode: {node}")
        print(f"HTMLNode: {html_node}")
        print(f"HTML: {html_node.to_html()}")
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This text should be italic")
        self.assertEqual(html_node.to_html(), "<i>This text should be italic</i>")

    def test_text_code(self):
        node = TextNode("This text should be in a code block", TextType.CODE)
        html_node = text_node_to_html_node(node)
        print("\nTextType.CODE to html")
        print(f"TextNode: {node}")
        print(f"HTMLNode: {html_node}")
        print(f"HTML: {html_node.to_html()}")
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This text should be in a code block")
        self.assertEqual(html_node.to_html(), "<code>This text should be in a code block</code>")

    def test_text_link(self):
        node = TextNode("This text should be a link", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        print("\nTextType.LINK to html")
        print(f"TextNode: {node}")
        print(f"HTMLNode: {html_node}")
        print(f"HTML: {html_node.to_html()}")
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This text should be a link")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">This text should be a link</a>')

    def test_text_image(self):
        node = TextNode("This text should be in the alt tag of an image", TextType.IMAGE, "../images/image.png")
        html_node = text_node_to_html_node(node)
        print("\nTextType.IMAGE to html")
        print(f"TextNode: {node}")
        print(f"HTMLNode: {html_node}")
        print(f"HTML: {html_node.to_html()}")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "" )
        self.assertEqual(html_node.props, {"src": "../images/image.png", "alt": "This text should be in the alt tag of an image"})
        self.assertEqual(html_node.to_html(), '<img src="../images/image.png" alt="This text should be in the alt tag of an image"></img>')

    def test_text_invalid_tag(self):
        # Create a ParentNode with no tag
        node = TextNode("This text should be in the alt tag of an image", "INVALID", "../images/image.png")
        print("\nInvalid TextType")
        print(f"TextNode: {node}")
        print("ValueError: Invalid text type: INVALID")
        with self.assertRaisesRegex(ValueError, "Invalid text type: INVALID"):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()