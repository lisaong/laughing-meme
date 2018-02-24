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

        def _row_data(self, row):
            "returns row data"
            HEADER_COLUMN = 0
            return [cell.text for cell in row.cells[HEADER_COLUMN+1:]]

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
            # Row indices in the docx table
            INDICES = ["category", "name", "description",
                "prof.level", "prof.code", "prof.desc",
                "prof.knowledge",  "prof.abilities", "prof.apps"]

            rows = self.table.rows

            self.name = self._row_data(rows[INDICES.index("name")])
            self.description = self._row_data(rows[INDICES.index("description")])

            # drop the repeated category cells
            self.category = self._row_data(rows[INDICES.index("category")])[0]

            # proficiency rows
            prof_level = self._row_data(rows[INDICES.index("prof.level")])
            prof_code = self._row_data(rows[INDICES.index("prof.code")])
            prof_desc = self._row_data(rows[INDICES.index("prof.desc")])
            prof_knowledge = self._row_data(rows[INDICES.index("prof.knowledge")])
            prof_abilities = self._row_data(rows[INDICES.index("prof.abilities")])
            prof_apps = self._row_data(rows[INDICES.index("prof.apps")])

            # match naming to the document
            self.proficiencies = [{ "level" : level, "TSC code" : code, \
                "TSC Proficiency Description" : desc, "Knowledge" : knowledge, \
                "Abilities" : abilities, "Range of Applications" : apps} \
                    for level, code, desc, knowledge, abilities, apps in \
                        zip(prof_level, prof_code, prof_desc, prof_knowledge,
                            prof_abilities, prof_apps)
            ]


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
