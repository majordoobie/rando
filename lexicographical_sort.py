"""
Make sure you set the right permissions to run this script 'chmod +x'
then call this script with the full path of your text file
example: "./ballsack.py /root/shitfile"

Sorts a list into lexicographical order 
"""
!/usr/bin/python

import sys
fuckingpath = str(sys.argv[1])
shitlist=open(fuckingpath).read().split()
shitlist=sorted(sorted(shitlist), key=str.upper)
for balls in shitlist:
	print(balls)
