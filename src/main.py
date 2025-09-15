from textnode import *
from htmlnode import *
from inline import *

def main():
    temp = TextNode("This is some `anchor` text", TextType.TEXT, "https://www.boot.dev")

    print(temp)

    split_nodes_delimited([temp], "`", TextType.CODE)

if __name__ == "__main__":
    main()