#!/usr/bin/python3

import argparse
import glob
import itertools
import json
import os

# pip install python-docx
import docx

def jsonify_tscs(root_path, json_outfile, json_format):
    """Extracts TSCs from multiple docx files into a json file"""

    class Tsc:
        "Encapsulates a TSC"
        def __init__(self, table):
            self.table = table
            self.name = None
            self.category = None
            self.description = None
            self.proficiencies = []
            self._extract()

        def _row_data(self, row):
            "returns row data"
            HEADER_COLUMN = 0
            return [cell.text for cell in row.cells[HEADER_COLUMN+1:]]

        def _extract(self):
            "Extracts a TSC from a docx table"

            # Row indices in the docx table
            INDICES = ["category", "name", "description",
                "prof.level", "prof.code", "prof.desc",
                "prof.knowledge",  "prof.abilities", "prof.apps"]

            rows = self.table.rows

            # drop the repeated category cells for these rows
            self.name = self._row_data(rows[INDICES.index("name")])[0]
            self.description = self._row_data(rows[INDICES.index("description")])[0]
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

    class TscEncoder(json.JSONEncoder):
        "Extends JSON encoding for a TSC"
        # Suppress false positive pylint "hidden" warning
        def default(self, obj):  # pylint: disable=E0202
            if isinstance(obj, Tsc):
                return {
                    # match naming to the document
                    "Name" : obj.name,
                    "Category" : obj.category,
                    "Description" : obj.description,
                    "Proficiencies" : obj.proficiencies
                }

            # Let the base class default method raise the TypeError
            return json.JSONEncoder.default(self, obj)

    def flatten_tscs(tscs):
        "Flattens a list of TSCs into proficiencies"
        return list(itertools.chain.from_iterable(
            [[{
                "TSC Name" : tsc.name,
                "TSC Category" : tsc.category,
                "TSC Description" : tsc.description,
                **p} for p in tsc.proficiencies]
            for tsc in tscs]
        ))

    def get_top_level_table(path):
        "Returns the top level table in the document, if any"
        try:
            doc = docx.Document(path)
            if doc.tables:
                print(path)
                return doc.tables[0]
        except:
            print("WARNING: Skipping invalid document {}".format(path))
        return None

    # main logic
    tscs = []
    for path in glob.glob("{}/**/*.docx".format(root_path),
        recursive=True):
        table = get_top_level_table(path)
        if table and table.rows:
            tscs.append(Tsc(table))

    with open(json_outfile, mode='w') as o:
        if json_format == "tabular":
            tscs = flatten_tscs(tscs)
        o.write(json.dumps(tscs, cls=TscEncoder, indent=4,
            ensure_ascii=True))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Converts the top level table in a .docx to JSON.')
    parser.add_argument('path',
        help='folder path to look for .docx files')
    parser.add_argument('--outfile',
        help="output file path (default: skillsmap_table.json)",
        default="skillsmap_table.json")
    parser.add_argument('--format',
        help="determines the json output format (default: tabular)",
        choices=["nested", "tabular"],
        default="tabular")
    args = parser.parse_args()
    jsonify_tscs(args.path, args.outfile, args.format)
