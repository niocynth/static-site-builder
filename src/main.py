from textnode import *
from htmlnode import *
from inline import *

def main():
    temp = "An ![image](../images/image.png) in a string (with brackets) and [square brackets] and a picture with no alt ![](../unicorn.gif)"

    extract_markdown_images(temp)

if __name__ == "__main__":
    main()