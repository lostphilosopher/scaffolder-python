#!/usr/local/bin/python

import sys

from writer import Writer

name = sys.argv[1]
type = sys.argv[2]

writer = Writer(name, type)

msg = writer.make()

print msg
