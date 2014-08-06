#!/usr/local/bin/python

from builder import Builder

builder = Builder('index.php', 'view')

print builder.getFilePath()

