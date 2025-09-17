from inline import *
from textnode import *
from htmlnode import *
from inline import *

def main():
    temp = "An ![image](../images/image.png) in a string (with brackets) and [square brackets] and a picture with no alt ![](../unicorn.gif)"

    extract_markdown_images(temp)

    node = TextNode("First ![img1](img1.png) then [link1](link.com) with [square brackets] and (brackets) and another [link2](https://hello.com) for good measure", TextType.TEXT)
    result = split_nodes_link([node])
    print(f"data in: {node}")
    print(f"final result: {result}")

if __name__ == "__main__":
    main()