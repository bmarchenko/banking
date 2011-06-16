#!/usr/bin/env python
import re

# the forbidden characters for names are:
# characters that are not letters, spaces or .
name_check = re.compile(r"[^A-Za-z\s\.]")

name = raw_input ("Please, enter your name: ")
while name_check.search(name):
    print "Please enter your name correctly!"
    name = raw_input ("Please, enter your name: ")
