#!/usr/bin/env python

alpha = 'abcdefghijklmnopqrstuvwxyz'
capitals = alpha.upper()
binbraille = ['100000', '110000', '100100', '100110', '100010', '110100', '110110', '110010', '010100', '010110', '101000', '111000', '101100', '101110', '101010', '111100', '111110', '111010', '011100', '011110', '101001', '111001', '010111', '101101', '101111', '101011']


string = 'The quick brown fox jumps over the lazy dog'
outstring = []
for i in range(len(string)):
	index = alpha.find(string[i])
	if index != -1:
		outstring.append( binbraille[index])
	elif capitals.find(string[i]) != -1:
		outstring.append( '000001'  )
		outstring.append( binbraille[capitals.find(string[i])] )
	else:
		outstring.append('000000')
print ''.join(outstring)

