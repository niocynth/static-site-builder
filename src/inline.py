from textnode import *
from htmlnode import *

def split_nodes_delimited(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        # Skip non-TEXT nodes
        if node.text_type != TextType.TEXT:
            result.append(node)
        elif delimiter not in node.text:
            raise Exception(f'Invalid Markdown syntax "{delimiter}"')
        else:
            split = []
            split.extend(node.text.split(delimiter))
            print(split)
            for i in range(len(split)):
                if i % 2 == 0 and split[i] != "":
                    result.append(TextNode(split[i], TextType.TEXT))
                elif i % 2 != 0 and split[i] != "":
                    result.append(TextNode(split[i], text_type))
    return result