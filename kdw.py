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
        self.path      = os.path.abspath(input)
        self.extension = os.path.splitext(input)[1]
        self.basename  = os.path.basename(input)
        self.filename  = self.basename.rsplit('.')[0]
        
        filename_components = self.filename.split('-')
        
        if len(filename_components) == 3:
            self.project   = filename_components[0]
            self.serial_no = filename_components[1]
            self.part_no   = filename_components[2]
            self.itemname  = "{0}-{1}".format(self.project, self.serial_no)
        else:
            self.project   = None
            self.serial_no = None
            self.part_no   = None
            self.itemname  = None


def main():
    print_banner()
    path_to_check = os.path.abspath(sys.argv[1])
    print('Checking "{0}"'.format(path_to_check))
    results = {'extra': []}

    for f in all_files(path_to_check):
        a = asset(f)
        if a.itemname is None:
            results['extra'].append(a)
        else:
            if a.itemname in results:
                results[a.itemname].append(a)
            else:
                results[a.itemname] = [a]

    for item, assets in [i for i in results.items() if i != 'extra']:
        components = set([a.part_no for a in assets])
        print("{0} -- {1} pages / {2} files".format(
            item, len(components), len(assets)
            ))
        for n in assets:
            print("  -> {0}".format(n.basename))

if __name__ == "__main__":
    main()
