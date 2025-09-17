import re
from textnode import *
from htmlnode import *

def split_nodes_delimited(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError("All nodes must be TextNode instances")
        # Skip non-TEXT nodes
        if node.text_type != TextType.TEXT:
            result.append(node)
        elif delimiter not in node.text:
            result.append(node)
        else:
            split = []
            split.extend(node.text.split(delimiter))
            if len(split) % 2 == 0:
                raise Exception("Invalid Markdown syntax")
            for i in range(len(split)):
                if i % 2 == 0 and split[i] != "":
                    result.append(TextNode(split[i], TextType.TEXT))
                elif i % 2 != 0 and split[i] != "":
                    result.append(TextNode(split[i], text_type))
    return result

def extract_markdown_images(text):
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError("All nodes must be TextNode instances")
        if node.text_type != TextType.TEXT or "![" not in node.text:
            result.append(node)
        else:
            images = extract_markdown_images(node.text)
            if len(images) == 0:
                result.append(node)
            else:
                split  = []
                alt, url = images[0]
                split.extend(re.split(r'!\[(.*?)\)', node.text, maxsplit=1))
                for i in range(3):
                    if i % 2 == 0 and split[i] != "":
                        result.append(TextNode(split[i], TextType.TEXT))
                    elif i % 2 != 0 and split[i] != "":
                        result.append(TextNode(alt, TextType.IMAGE, url))
                result = split_nodes_image(result)
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError("All nodes must be TextNode instances")
        if node.text_type != TextType.TEXT or "[" not in node.text:
            result.append(node)
        else:
            links = extract_markdown_links(node.text)
            if len(links) == 0:
                result.append(node)
            else:
                split  = []
                text, url = links[0]
                split.extend(re.split(r'(?<!\!)\[[^\]]+\]\([^)]+\)', node.text, maxsplit=1))
                split.insert(1, "")
                print(f"split: {split}")
                for i in range(3):
                    if i % 2 == 0 and split[i] != "":
                        result.append(TextNode(split[i], TextType.TEXT))
                    elif i % 2 != 0:
                        result.append(TextNode(text, TextType.LINK, url))
                result = split_nodes_link(result)
    return result

def text_to_textnodes(text):
    text = TextNode(text, TextType.TEXT)
    result = []
    result = split_nodes_delimited([text], "**", TextType.BOLD)
    result = split_nodes_delimited(result, "_", TextType.ITALIC)
    result = split_nodes_delimited(result, "`", TextType.CODE)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result
                            