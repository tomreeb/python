#!/usr/local/bin/python

# usage: test.py -[m,t] <sourcefile>

import os, sys, getopt, readline

from shutil import copyfile

def main(argv):
   sourcefile = ''
   try:
      opts, args = getopt.getopt(argv,"hm:t:v:")
   except getopt.GetoptError:
      print 'usage: test.py -[m,t] <sourcefile>'
      sys.exit(2)
   for opt, arg in opts:
      sourcefile = arg
      # Get full path of file
      sourcepath = os.path.abspath(sourcefile)
      # Take file name, split from right once giving me the extension and everything else. Print the second thing [1]
      filext = sourcefile.rsplit(".",1)[1]
      if opt == "-v":
         destdir = '/home/serveradmin/Videos/'
         os.chdir(destdir)
         readline.parse_and_bind("tab: complete")
         vpath = raw_input("Enter the path for the video: ")
         vname = raw_input("Enter the name for the video: ")
         destfile = str(vname)+'.'+filext
         destpath = str(destdir)+str(vpath)+'/'+destfile
         
         # Create dirs if they do not exist
         if not os.path.exists(os.path.dirname(destpath)):
            try:
               os.makedirs(os.path.dirname(destpath))
            except OSError as exc: # Guard against race condition
              if exc.errno != errno.EEXIST:
                 raise
         
         print "Full name: %s" %(str(destfile))
         print "Copy from: %s" %(str(sourcepath))
         print "Copy to: %s" %(str(destpath))
         if os.path.exists(destpath):
            raise Exception("Destination file exists!")
         else:
            copyfile(sourcepath, destpath)
         
if __name__ == "__main__":
   main(sys.argv[1:])