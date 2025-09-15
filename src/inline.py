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
            temp = node.text.split(delimiter)
            print(temp)
        
    print(result)