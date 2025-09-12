import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        prop = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(None, None, None, prop)
        result = node.props_to_html()
        validation = ' href="https://www.google.com" target="_blank"'
        print(f"\nResult: {result}")
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
        print(f"\nResult: {result}")
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
        print(f"\nResult: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)

    def test_props_to_html_no_props(self):
        prop = None
        node = HTMLNode(None, None, None, prop)
        result = node.props_to_html()
        validation = ''
        print(f"\nResult: {result}")
        print(f"Validation: {validation}")
        self.assertEqual(validation, result)