#! /usr/bin/python

import sys, os, re
import fileinput
from optparse import OptionParser

def grep():
    usage = "Usage: %prog [options] PATTERN ..."
    parser = OptionParser(usage=usage)
    parser.add_option("-r", "--recursive", dest="recursive", action="store_true",
                      help="Read all files under each directory, recursively")
    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.print_help()
        exit(1)
    pat = re.compile(args[0])
    for line in fileinput.input(args[1:]):
        if pat.search(line):
            sys.stdout.write("%s:%d:%s" % (fileinput.filename(), fileinput.lineno(), line))
    return 0

if __name__ == '__main__':
    exit(grep())
