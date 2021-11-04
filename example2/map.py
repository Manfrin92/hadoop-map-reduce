#!/usr/bin/env python
import sys

for row in sys.stdin:
    fields = row.split(';');

    id = fields[0];
    idAuthor = fields[1];
    CreationDate = fields[2];
    Tweet = fields[3];

    if "Empresa1" in Tweet and "worst" not in Tweet and "bad" not in Tweet and "never" not in Tweet and "horrible" not in Tweet and "terrible" not in Tweet and "?" not in Tweet:
        print '%s\t%s' % ("Empresa1", "1");
		
