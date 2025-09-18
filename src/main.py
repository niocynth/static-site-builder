import os
import shutil
from inline import *
from textnode import *
from htmlnode import *
from inline import *
from block import *

def clean_public_dir():
    abs_public = os.path.abspath("public")
    if os.path.exists(abs_public):
        shutil.rmtree(abs_public)
    os.mkdir(abs_public, mode=0o755)


def clone_files_to_public(path, abs_root=None):
    abs_public = os.path.abspath("public")
    abs_path = os.path.abspath(path)
    if abs_root is None:
        abs_root = abs_path
    if not os.path.exists(abs_public) or os.listdir(abs_public) != []:
        clean_public_dir()
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"The path '{path}' does not exist.")
    if os.listdir(abs_path) == []:
        return
    for item in os.listdir(abs_path):
        abs_item = os.path.join(abs_path, item)
        item_path = os.path.relpath(abs_item, abs_root)
        dest_path = os.path.join(abs_public, item_path)
        if os.path.isdir(abs_item):
            os.makedirs(dest_path, mode=0o755, exist_ok=True)
            clone_files_to_public(abs_item, abs_root)
        elif os.path.isfile(abs_item):
            os.makedirs(os.path.dirname(dest_path), mode=0o755, exist_ok=True)
            shutil.copy(abs_item, dest_path)

def extract_title(markdown):
    for lines in markdown.splitlines():
        if lines.startswith("# "):
            return lines[2:].strip()
    raise Exception("No title found in the markdown content")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from '{from_path}' to '{dest_path}' using template '{template_path}'")
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    markdown_file.close()
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    content = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content.to_html())
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path), mode=0o755, exist_ok=True)
    output_file = open(dest_path, "w")
    output_file.write(html)
    output_file.close()



def main():
    clone_files_to_public("static")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()