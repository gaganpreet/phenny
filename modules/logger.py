#!/usr/bin/env python
"""
logger.py - Phenny Logger Module
Author: Gaganpreet, http://gaganpreet.in
"""
import time, os;

def logger(phenny, input): 
    file = open(os.path.expanduser("~/.phenny/log_%s.txt"%(input.sender)), "a");
    file.write(time.ctime() + " <" + input.nick + "> " + input + "\n");
    file.close();
logger.rule = r'.*'

if __name__ == '__main__': 
   print __doc__.strip()
