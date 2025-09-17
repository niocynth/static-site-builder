from inline import *
from textnode import *
from htmlnode import *
from inline import *

def main():
    temp = "An ![image](../images/image.png) in a string (with brackets) and [square brackets] and a picture with no alt ![](../unicorn.gif)"

    extract_markdown_images(temp)

    node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    result = text_to_textnodes(node)
    print(f"data in: {node}")
    print(f"final result: {result}")

if __name__ == "__main__":
    main()