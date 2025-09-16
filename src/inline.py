import re
from textnode import *
from htmlnode import *

def split_nodes_delimited(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
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