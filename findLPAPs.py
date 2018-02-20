#!/usr/bin/python3

import argparse
import collections
import glob
import itertools
import os
import re

def find_files(path, count, search_count):
    "Finds files from a path"
    d = dict()

    for filename in glob.iglob('{}/**/*LPAP*.docx'.format(path), recursive=True):
        if not re.search('Archive', filename) and not re.search('LPAP_Sample', filename):
            ctime = os.path.getctime(filename) # assumes Windows platform
            size = os.path.getsize(filename)
            d[ctime * size / 1000] = filename
            print('{} {}: {}'.format(ctime, size, filename))
        search_count = search_count-1
        if search_count == 0:
            break
    return collections.OrderedDict(\
        itertools.islice(sorted(d.items(), key=lambda t: t[0], reverse=True), count))

parser = argparse.ArgumentParser(
    description='Lists LPAP files, sorted by date and size.')
parser.add_argument('path', help='folder path to search')
parser.add_argument('--count', '-c', help='max number of files to return', type=int,
    default=10)
parser.add_argument('--search_count', '-s', help='max number of files to search',
    type=int, default=100)
args = parser.parse_args()
result = find_files(args.path, args.count, args.search_count)
print(result.items())
