from textnode import *
from htmlnode import *

def main():
    temp = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

    print(temp)

if __name__ == "__main__":
    main()