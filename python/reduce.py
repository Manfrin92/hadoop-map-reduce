#!/usr/bin/env python
import sys

occurrency = {}
for row in sys.stdin:
    key, value = row.split('\t', 1);

    try:
        value = int(value);
    except ValueError:
        continue;
    try:
        occurrency[key] = occurrency[key] + value;
    except Exception, e:
        print str(e);
        occurrency[key] = value;

for country in occurrency.keys():
    print '%s\t%s' % (occurrency[country], country);
