#!/usr/bin/python3

import argparse
import collections
import glob
import itertools
import os

def find_files(path, count, search_count):
    "Finds files from a path"
    d = dict()
    for filename in glob.iglob('{}/**/*LPAP*.docx'.format(path), recursive=True):
        # assumes Windows platform
        # assumes files modified at the same time will override (don't care for now)
        d[os.path.getctime(filename)] = filename
        search_count = search_count-1
        if search_count == 0:
            break
    return collections.OrderedDict(itertools.islice(sorted(d.items(), key=lambda t: t[0]), count))

parser = argparse.ArgumentParser(description='Lists LPAP files, sorted by date and size.')
parser.add_argument('path', help='folder path to search')
parser.add_argument('--count', '-c', help='max number of files to return', type=int, default=10)
parser.add_argument('--search_count', '-s', help='max number of files to search', type=int, default=100)
args = parser.parse_args()
result = find_files(args.path, args.count, args.search_count)
print(result.items())
