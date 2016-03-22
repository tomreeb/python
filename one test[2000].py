#!/usr/local/bin/python

# usage: test.py -[m,t] <sourcefile>

import os, sys, getopt

def main(argv):
   sourcefile = ''
   try:
      opts, args = getopt.getopt(argv,"m:t:")
   except getopt.GetoptError:
      print 'usage: test.py -[m,t] <sourcefile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'usage: test.py -[m,t] <sourcefile>'
         sys.exit()
      elif opt in ("-m"):
         sourcefile = arg
         filext = sourcefile.split(".")[0]
         print sourcefile
         print filext
         
if __name__ == "__main__":
   main(sys.argv[1:])