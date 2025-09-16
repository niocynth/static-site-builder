from inline import *
from textnode import *
from htmlnode import *
from inline import *

def main():
    temp = "An ![image](../images/image.png) in a string (with brackets) and [square brackets] and a picture with no alt ![](../unicorn.gif)"

    extract_markdown_images(temp)

    node = TextNode("First ![img1](img1.png) then ![img2](img2.jpg).", TextType.TEXT)
    split_nodes_image([node])

if __name__ == "__main__":
    main()