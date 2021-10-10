#!/usr/bin/env python
import sys

for row in sys.stdin:
    fields = row.split(';');

    country = fields[0];
    year = fields[1];
    code = fields[2];
    commodity = fields[3];
    flux = fields[4];
    value = fields[5];
    weight = fields[6];
    unit = fields[7];
    quantity = fields[8];
    category = fields[9];

    # What will be generated as key value and should be usedin the Shuffle function (automatic one)

    print '%s\t%s' % (year+commodity, weight);
