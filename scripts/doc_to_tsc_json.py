#!/usr/bin/python3

import argparse
import glob
import json
import os

# pip install python-docx
import docx

def jsonify_top_level_table(root_path):
    """Converts the top level table of a docx to json"""

    class Tsc:
        "Encapsulates a TSC"
        def __init__(self, table):
            self.table = table
            self.name = None
            self.category = None
            self.description = None
            self.proficiencies = []
            self._extract()

        def as_json(self):
            "returns the TSC as a json object"

        def _extract_row(self, row):
            "returns row data as a tuple of header, data"
            HEADER_COLUMN = 0
            header = row.cells[HEADER_COLUMN].text
            data = [cell.text for cell in row.cells[HEADER_COLUMN+1:]]
            return (header, data)

        def _extract(self):
            """Extracts information from a docx table:
                  Category
                  Description
                  Proficiencies (list)
                    Level
                    TSC Code
                    Knowledge (list)
                    Abilities (list)
                    Range of Applications (list)
            """
            # doc-format specific constants
            CATEGORY_ROW = 0
            NAME_ROW = 1
            rows = self.table.rows

            self.name = self._extract_row(rows[NAME_ROW])
            self.category = self._extract_row(rows[CATEGORY_ROW])

    def get_top_level_table(path):
        "Returns the top level table in the document, if any"
        doc = docx.Document(path)
        if doc.tables:
            print(path)
            return doc.tables[0]
        return None

    def table_to_json(table=None):
        "Converts the table to JSON"
        if table and table.rows:
            tsc = Tsc(table)
            return tsc.as_json()

    for path in glob.glob("{}/**/*.docx".format(root_path),
        recursive=True):
        print(table_to_json(get_top_level_table(path)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Converts the top level table in a .docx to JSON.'
        "This JSON can be read by something like http://www.jsondata.ninja/")
    parser.add_argument('path',
        help='folder path to look for .docx files')
    args = parser.parse_args()
    jsonify_top_level_table(args.path)
