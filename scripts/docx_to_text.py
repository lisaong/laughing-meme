#!/usr/bin/python3

import argparse
import glob
import os
import re

# pip install docx2txt
import docx2txt

def convert(root_path):
    """Converts .docx files under root_path to .txt"""

    def save_as_text(path):
        "Helper function that saves a .docx to .txt"

        text_path = re.sub(r'\.\w+$', '.txt',
            os.path.abspath(path))

        # extract text and write to output file
        with open(text_path, 'w') as out:
            out.write(docx2txt.process(path))

        print("{} -> {}".format(path, text_path))

    # Create list of paths to .doc files
    for path in glob.glob("{}/**/*.docx".format(root_path),
        recursive=True):
        save_as_text(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Converts .docx to txt.')
    parser.add_argument('path',
        help='folder path to look for .docx files')
    args = parser.parse_args()
    convert(args.path)
