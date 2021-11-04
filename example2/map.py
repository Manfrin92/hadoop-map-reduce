#!/usr/bin/env python
import sys

for row in sys.stdin:
    fields = row.split(';');

    id = fields[0];
    idAuthor = fields[1];
    CreationDate = fields[2];
    Tweet = fields[3];

    if "Empresa1" in Tweet and "contact" in Tweet:
        print '%s\t%s' % ("Empresa1", "1");
		
