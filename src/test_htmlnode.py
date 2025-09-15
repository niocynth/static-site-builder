import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    # HTMLNode tests
    def test_props_to_html(self):
        prop = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(None, None, None, prop)
        result = node.props_to_html()
        validation = ' href="https://www.google.com" target="_blank"'
        print("\nprops_to_html 2 props")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_props_to_html_2(self):
        prop = {
            "rel": "shortcut icon",
            "type": "image/png/ico",
            "href": "/favicon.ico"
        }
        node = HTMLNode(None, None, None, prop)
        result = node.props_to_html()
        validation = ' rel="shortcut icon" type="image/png/ico" href="/favicon.ico"'
        print(f"\nprops_to_html 3 props")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_props_to_html_no_value(self):
        prop = {
            "src": "app/asset-manifest.json.js",
            "async": None,
            "nonce": "05d5a2cd32cfa2b3d7ff2cc75c1e0b1bd0b38591"
        }
        node = HTMLNode(None, None, None, prop)
        result = node.props_to_html()
        validation = ' src="app/asset-manifest.json.js" async nonce="05d5a2cd32cfa2b3d7ff2cc75c1e0b1bd0b38591"'
        print("\nprops_to_html prop no value")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_props_to_html_no_props(self):
        prop = None
        node = HTMLNode(None, None, None, prop)
        result = node.props_to_html()
        validation = ''
        print("\nprops_to_html with no props")
        print(f"Result: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    # LeafNode tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        print("\nLeafNode.to_html")
        print(f"Result: {node.to_html()}")
        print(f"Validation: <p>Hello, world!</p>")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "google.com", {"href": "https://www.google.com"})
        print("\nLeafNode.to_html with props")
        print(f"Result: {node.to_html()}")
        print(f'Validation: <a href="https://www.google.com">google.com</a>')
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">google.com</a>')

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Ohayo Gozaimasu!")
        print("\nLeafNode.to_html different tag")
        print(f"Result: {node.to_html()}")
        print("Validation: <h1>Ohayo Gozaimasu!</h1>")
        self.assertEqual(node.to_html(), "<h1>Ohayo Gozaimasu!</h1>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello World!")
        print("\nLeafNode.to_html no tag")
        print(f"Result {node.to_html()}")
        print("Validation: Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")

    def test_leaf_to_html_no_value(self):
        # Create a LeafNode with no value (or None as value)
        node = LeafNode("p", None)
        print("\nLeafNode.to_html no value")
        print("ValueError: All leaf nodes must have a value")
        with self.assertRaisesRegex(ValueError, "All leaf nodes must have a value"):
            node.to_html()

    # ParentNode tests
    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        print("\nParentNode.to_html with children")
        print(f"Result: {parent_node.to_html()}")
        print("Validation: <div><span>child</span></div>")
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        print("\nParentNode.to_html with grandchildren")
        print(f"Result: {parent_node.to_html()}")
        print("Validation: <div><span><b>grandchild</b></span></div>")
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_parent_to_html_with_no_children(self):
        # Create a ParentNode with no children
        parent_node = ParentNode("div", None)
        print("\nParentNode.to_html no children")
        print("ValueError: All parent nodes must have children")
        with self.assertRaisesRegex(ValueError, "All parent nodes must have children"):
            parent_node.to_html()
        
    def test_parent_to_html_with_no_tag(self):
        # Create a ParentNode with no tag
        child_node = LeafNode(None, "Hello World")
        parent_node = ParentNode(None, [child_node])
        print("\nParentNode.to_html no tag")
        print("ValueError: All parent nodes must have a tag")
        with self.assertRaisesRegex(ValueError, "All parent nodes must have a tag"):
            parent_node.to_html()