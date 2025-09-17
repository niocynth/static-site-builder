from inline import *
from textnode import *
from htmlnode import *
from inline import *
from block import *

def main():

    md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.




- This is the first list item in a list block
- This is a list item
- This is another list item

"""
    print(markdown_to_blocks(md))

if __name__ == "__main__":
    main()