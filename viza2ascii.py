# -*- coding: utf-8 -*-
#
# viza2ascii.py
# 
# Created on: 16.11.2019
# Author: t33bu (Teemu Leppänen, tjlepp@gmail.com)
#
# This work is licensed under Creative Commons
# Attribution-NonCommercial-ShareAlike (CC BY-NC-SA 4.0)
# https://creativecommons.org/licenses/by-nc-sa/4.0/

import sys

ctrl = { 
        0x0d: '\n',
        0x20: ' ',
        0x21: '!',
        0x22: '\"',
        0x23: '#',
        0x24: '$',
        0x25: '%',
        0x26: '&',        
        0x27: '\'',
        0x28: '(',
        0x29: ')',
        0x2a: '*',
        0x2b: '+',
        0x2c: ',',
        0x2d: '-',
        0x2e: '.',
        0x2f: '/',
        0x3a: ':',
        0x3b: ';',
        0x3c: '<',        
        0x3d: '=',
        0x3e: '>',
        0x3f: '?',        
        0x40: '@',
        0x5b: '[',
        0x5c: '£',
        0x5d: ']',
        0xdc: '\n', # not sure?
        0xeb: '\t', # not sure?
        0xf1: '\f' # form feed?
        }

locals = {
         0x72: 'Ö',
         0x73: 'Ä',
         0x78: 'ö',
         0x79: 'ä'
         }

if len(sys.argv) != 2:
    sys.exit("ERROR: Input filename not given")

filename = sys.argv[1]
print("Processing " + filename)

filein = open(filename,"rb")
document = list(filein.read())
document = document[2:] # get rid of prg-format
filein.close()

ascii = []

for d in document:
    # a-z
    if d > 0x00 and d < 0x1b:
        ascii.append(chr(d+0x60))
    # 0-9
    elif d > 0x29 and d < 0x3a:
        ascii.append(chr(d))
    # A-Z
    elif d > 0x40 and d < 0x5b:
        ascii.append(chr(d))
    # localized keys
    elif d in locals:
        ascii.append(locals[d])
    # control characters
    elif d in ctrl:
        ascii.append(ctrl[d])  
    # if all else fails
    else:
        ascii.append("["+hex(d)+"]")

outfilename = filename.split('.')[0] + ".txt"
print("Writing to " + outfilename)

fileout = open(outfilename,"wb")
fileout.write(bytes("".join(ascii),'utf-8'))
fileout.close()
        