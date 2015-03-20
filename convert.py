#!/usr/bin/env python

import re
import sys

def split(regex, lines):
    out = []
    for line in lines:
        line = line.strip()
        sline = re.split(regex, line)
        out.extend(sline)
    return out

def indent(line):
    regexp = re.compile('{{\s*if[^}]*}}')
    if regexp.search(line) is not None:
        return 1
    regexp = re.compile('{{\s*range[^}]*}}')
    if regexp.search(line) is not None:
        return 1
    return 0

def unindent(line):
    regexp = re.compile('{{\s*end[^}]*}}')
    if regexp.search(line) is not None:
        return -1
    return 0

def main():
    inf = sys.stdin
    lines = split('({{\s*if[^}]*}})', inf)
    lines = split('({{\s*range[^}]*}})', lines)
    lines = split('({{\s*end[^}]*}})', lines)
    lines = [line for line in lines if line.strip()]
    out = []
    tabs = 0
    for line in lines:
        line = line.strip()
        print(unindent(line))
        tabs = tabs + unindent(line)
        line = ("\t" * tabs) + line
        out.append(line)
        tabs = tabs + indent(line)
    for line in out:
        print(line)

if __name__ == "__main__":
        main()
