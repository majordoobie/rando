"""
simulates a stat command in nix for winders
"""

#!/usr/bin/python
#Argument is the full path to the file
import os.path, time
import sys 

path = str(sys.argv[1])
print "last modified: %s" % time.ctime(os.path.getmtime(path))
print "last change: %s" % time.ctime(os.path.getctime(path))
print "last accessed: %s" %time.ctime(os.path.getatime(path))
