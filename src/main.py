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




def main():
    clone_files_to_public("static")    

if __name__ == "__main__":
    main()