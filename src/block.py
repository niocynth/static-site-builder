from enum import Enum
from textnode import *
from htmlnode import *
from inline import *

def markdown_to_blocks(markdown):
    blocks = []
    temp_blocks = markdown.split("\n\n")
    for block in temp_blocks:
        block = block.strip()
        if block != "":
            blocks.append(block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ORDERED_LIST = "ordered_list"
    UNORDERED_LIST = "unordered_list"

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif re.match(r"^>", block):
        return BlockType.QUOTE
    elif re.match(r"^\d+\. ", block):
        return BlockType.ORDERED_LIST
    elif re.match(r"^[-*+] ", block):
        return BlockType.UNORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def text_to_children(content):
    inline_nodes = text_to_textnodes(content)
    html_children = []
    for inline_node in inline_nodes:
        html_children.append(text_node_to_html_node(inline_node))
    return html_children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            level = len(re.match(r"^(#{1,6}) ", block).group(1))
            content = block[level+1:].strip()
            children = text_to_children(content)
            nodes.append(ParentNode(f"h{level}", children))
        elif block_type == BlockType.CODE:
            content = block[3:-3].strip()
            nodes.append(ParentNode("pre", [LeafNode("code", content)]))
        elif block_type == BlockType.QUOTE:
            content = re.sub(r"^> ?", "", block, flags=re.MULTILINE).strip()
            children = text_to_children(content)
            nodes.append(ParentNode("blockquote", children))
        elif block_type == BlockType.ORDERED_LIST:
            items = re.findall(r"^\d+\. (.+)$", block, flags=re.MULTILINE)
            li_children = []
            for item in items:
                children = text_to_children(item.strip())
                li_children.append(ParentNode("li", children))
            nodes.append(ParentNode("ol", li_children))
        elif block_type == BlockType.UNORDERED_LIST:
            items = re.findall(r"^[-*+] (.+)$", block, flags=re.MULTILINE)
            li_children = []
            for item in items:
                children = text_to_children(item.strip())
                li_children.append(ParentNode("li", children))
            nodes.append(ParentNode("ul", li_children))
        else:  # Paragraph
            content = block.strip()
            children = text_to_children(content)
            nodes.append(ParentNode("p", children))
    return ParentNode("div", nodes)
