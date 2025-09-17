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

