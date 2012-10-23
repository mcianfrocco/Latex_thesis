#!/usr/bin/env python

import linecache 
import sys

f = sys.argv[1]

openF = open(f,'r')
totalLines = len(openF.readlines())

i = 1

while i <= totalLines:

	lineQ = linecache.getline(f,i)
	
	testLength = len(lineQ)

	if testLength == 1:
		print lineQ[:-1]
		i = i + 1
		continue
	
	lineInfo = lineQ.split()
	
	if lineInfo[0] == 'author' and lineInfo[1] == '=':
		author = lineInfo[2]
		author = author[1:-1]		
		print '@article{%s_%s,' %(author,str(i)) 
		print lineQ[:-1]

	if lineInfo[0] == 'title' and lineInfo[1] == '=':
		print lineQ[:-1]

	if lineInfo[0] == 'journal' and lineInfo[1] == '=':
		print lineQ[:-1]
	
	if lineInfo[0] == 'volume' and lineInfo[1] == '=':
		print lineQ[:-1]

	if lineInfo[0] == 'number' and lineInfo[1] == '=':
		print lineQ[:-1]

	if lineInfo[0] == 'pages' and lineInfo[1] == '=':
		print lineQ[:-1]

	if lineInfo[0] == 'year' and lineInfo[1] == '=':
		print '%s}' %(lineQ[:-1])

	i = i + 1
