#!/usr/local/bin/python
#
# Media File Copy Script
# By: Tom Reeb, March 22nd 2016
#
# The purpose of this script is to copy and rename a file based on the type.
# We are handling three different types of files: Movies, TV Episodes, and Misc. Videos.
#
# usage: python media_copy.py -[h,m,t,v] <sourcefile>
#
# Movies (-m flag) are copied to /data/media/Movies and renamed "Movie Name [YEAR].ext
# TV Episodes (-t flag) are copied to /data/media/TV/Show Name/Season X/SXXEXX.ext
# Videos (-v flag) are copied to /data/media/Videos/user/defined/path/video name.ext
#
# Future consideration will be handling a dump of an entire tv series

import os, sys, getopt, readline

from shutil import copyfile

def main(argv):
   sourcefile = ''
   try:
      opts, args = getopt.getopt(argv,"hm:t:v:")
   except getopt.GetoptError:
      print 'Invalid option'
      print 'Try -h for more information'
      sys.exit(2)
   for opt, arg in opts:
      sourcefile = arg
      sourcepath = os.path.abspath(sourcefile)  # Gets full path of file
      if opt == '-h':
         print 'usage: media_copy.py -[m,t,v] <sourcefile>'
         print ''
         print 'Options and arguments'
         print ' -m     : Movies (-m flag) are copied to /data/media/Movies and renamed Movie Name[YEAR].ext'
         print ' -t     : TV Episodes (-t flag) are copied to /data/media/TV/Show Name/Season X/ and renamed SXXEXX.ext'
         print ' -v     : Videos (-v flag) are copied to /data/media/Videos/user/defined/path/ and renamed Video Name.ext'
         sys.exit()
      elif opt == "-m":
         filext = sourcefile.rsplit(".",1)[1]   # Take file name and split from right into 2 parts. Use the second part [1], which is the extension
         destdir = '/data/media/Movies/'
         mname = raw_input("Enter the name of the Movie: ")
         myear = raw_input("Enter the year of the Movie: ")
         destfile = str(mname)+'['+str(myear)+'].'+filext
         destpath = str(destdir)+str(mname)+'['+str(myear)+'].'+filext
         print "Full name: %s" %(str(destfile))
         print "Copy from: %s" %(str(sourcepath))
         print "Copy to: %s" %(str(destpath))
         copyfile(sourcepath, destpath)
      elif opt == "-t":
         filext = sourcefile.rsplit(".",1)[1]
         destdir = '/data/media/TV/'
         os.chdir(destdir)              # These two lines are for tab compeltion, makes things easier
         readline.parse_and_bind("tab: complete")
         tname = raw_input("Enter the name of the Show: ")
         tseason = int(input("Enter the season number: "))
         tepisode = int(input("Enter the episode number: "))
         # the "%02d"%var will convert a single digit to two i.e. 1 = 01
         destfile = 'S'+str("%02d"%tseason)+'E'+str("%02d"%tepisode)+'.'+filext
         destpath = str(destdir)+str(tname)+'/Season '+str(tseason)+'/'+destfile
         
         # Create dirs if show and/or season do not exist
         if not os.path.exists(os.path.dirname(destpath)):
            try:
               os.makedirs(os.path.dirname(destpath))
            except OSError as exc: # Guard against race condition
              if exc.errno != errno.EEXIST:
                 raise
         
         print "Full name: %s" %(str(destfile))
         print "Copy from: %s" %(str(sourcepath))
         print "Copy to: %s" %(str(destpath))
         copyfile(sourcepath, destpath)
      elif opt == "-v":
         filext = sourcefile.rsplit(".",1)[1]
         destdir = '/data/media/Videos/'
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
         copyfile(sourcepath, destpath)
         
if __name__ == "__main__":
   main(sys.argv[1:])