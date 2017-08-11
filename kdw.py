#!/usr/bin/env python3

import os
import sys


def print_banner():
    '''Print a small banner to the console'''
    banner = "| KAP Data Wrangler |"
    bar = '=' * len(banner)
    print('\n'.join(['', bar, banner, bar, '']))


def all_files(start_dir):
    '''Generator yields all visible files in path'''
    for root, dirs, files in os.walk(start_dir):
        for f in files:
            if not f.startswith('.') and not f == "Thumbs.db":
                yield os.path.join(root, f)


class asset:
    '''Class representing an digital asset'''
    def __init__(self, input):
        self.path = os.path.abspath(input)
        self.extension = os.path.splitext(input)[1]
        self.basename = os.path.basename(input)
        self.filename = self.basename.rsplit('.')[0]
        (self.project, self.filnum, self.component) = self.filename.split('-')
        


def main():
    print_banner()
    path_to_check = os.path.abspath(sys.argv[1])
    print('Checking "{0}"'.format(path_to_check))
    for f in all_files(path_to_check):
        print(f)
        a = asset(f)
        print(a.project, a.filnum, a.component, a.extension)

if __name__ == "__main__":
    main()
