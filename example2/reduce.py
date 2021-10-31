#!/usr/bin/env python
import sys

ocorrencia = {}
for row in sys.stdin:
	key, value = row.split('\t', 1);

	try:
		value = int(value);
	except ValueError:		
		continue;
	try:
		ocorrencia[key] = ocorrencia[key] + value;		
	except Exception, e:
		print str(e);		
		ocorrencia[key] = value;

for country in ocorrencia.keys():
	print '%s\t%s' % (ocorrencia[country], country);
