#!/usr/bin/python3

import argparse
import glob
import os
import re

import win32com.client as win32
from win32com.client import constants

def convert(root_path):
    """Converts .doc files under root_path to .docx"""

    def save_as_docx(doc_path):
        "Helper function that saves a .doc to .docx"

        # open doc in word
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(path)
        doc.Activate()

        docx_path = re.sub(r'\.\w+$', '.docx',
            os.path.abspath(doc_path))
        word.ActiveDocument.SaveAs(
            docx_path, FileFormat=constants.wdFormatXMLDocument)
        doc.Close(False)
        print("{} -> {}".format(path, docx_path))

    # Create list of paths to .doc files
    for path in glob.glob("{}/**/*.doc".format(root_path),
        recursive=True):
        save_as_docx(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Converts .doc to docx.')
    parser.add_argument('path',
        help='folder path to look for .doc files')
    args = parser.parse_args()
    convert(args.path)
