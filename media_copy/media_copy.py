#!/usr/bin/env python

import os, sys, getopt, readline

from shutil import copyfile

def main(argv):
    sourcefile = ''
    supportedFiletypes = [ 'mkv', 'avi', 'mp4', 'mov', 'mpg', 'mpeg', 'm4v' ]
    try:
        opts, args = getopt.getopt(argv,"hm:t:v:f:")
    except getopt.GetoptError as err:
        print str(err)
        print 'Try -h for more information'
        sys.exit(2)
    for opt, arg in opts:
        sourcefile = arg
        sourcepath = os.path.abspath(sourcefile)                                                  # Gets full path of file
        if opt == '-h':
            print 'usage: python media_copy.py -[m,t,f,v] <source>'
            print ''
            print 'Options and arguments'
            print ' -m     : Movies are copied to /data/media/Movies and renamed Movie Name[YEAR].ext'
            print ' -t     : Individual TV Episodes are copied to /data/media/TV/Show Name/Season X/ and renamed SXXEXX.ext'
            print ' -f     : Same as above but will loop through directory and copy files sequentially'
            print ' -v     : Videos are copied to /data/media/Videos/user/defined/path/ and renamed Video Name.ext'
            sys.exit()
        elif opt == "-m":
            filext = sourcefile.rsplit(".",1)[1]                                                   # Take file name and split from right into 2 parts. Use the second part [1], which is the extension
            destdir = '/data/media/Movies/'
            mname = raw_input("Enter the name of the Movie: ")
            myear = raw_input("Enter the year of the Movie: ")
            destfile = str(mname)+'['+str(myear)+'].'+filext
            destpath = str(destdir)+str(mname)+'['+str(myear)+'].'+filext
            print "Copying %s" %(str(sourcepath))
            print "To %s" %(str(destpath))
            if os.path.exists(destpath):                                                           # Don't overwrite existing files
                raise Exception("Destination file exists!")
            else:
                copyfile(sourcepath, destpath)
        elif opt == "-t":
            filext = sourcefile.rsplit(".",1)[1]
            destdir = '/data/media/TV/'
            os.chdir(destdir)                                                                      # These two lines are for tab compeltion, makes things easier
            readline.parse_and_bind("tab: complete")
            tname = raw_input("Enter the name of the Show: ")
            tseason = int(input("Enter the season number: "))
            tepisode = int(input("Enter the episode number: "))
            destfile = 'S'+str("%02d"%tseason)+'E'+str("%02d"%tepisode)+'.'+filext                 # the "%02d"%var will convert a single digit to two i.e. 1 = 01
            destpath = str(destdir)+str(tname)+'/Season '+str(tseason)+'/'+destfile

            if not os.path.exists(os.path.dirname(destpath)):                                      # Create dirs if show and/or season do not exist
                try:
                    os.makedirs(os.path.dirname(destpath))
                except OSError as exc:                                                             # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise

            print "Copying %s" %(str(sourcepath))
            print "To %s" %(str(destpath))
            if os.path.exists(destpath):
                raise Exception("Destination file exists!")
            else:
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

            if not os.path.exists(os.path.dirname(destpath)):
                try:
                    os.makedirs(os.path.dirname(destpath))
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise

            print "Copying %s" %(str(sourcepath))
            print "To %s" %(str(destpath))
            if os.path.exists(destpath):
                raise Exception("Destination file exists!")
            else:
                copyfile(sourcepath, destpath)
        elif opt == "-f":
            destdir = '/data/media/TV/'
            os.chdir(destdir)
            readline.parse_and_bind("tab: complete")
            tname = raw_input("Enter the name of the Show: ")
            tseason = int(input("Enter the season number: "))
            tepisode = 0
            for subdir, dirs, files in os.walk(sourcefile):
                for file in files:
                    filext = file.rsplit(".",1)[1]
                    if filext in supportedFiletypes:                                               # Only copy media files
                        tepisode = tepisode + 1                                                    # Episode number iteration
                        destfile = 'S'+str("%02d"%tseason)+'E'+str("%02d"%tepisode)+'.'+filext
                        destpath = str(destdir)+str(tname)+'/Season '+str(tseason)+'/'+destfile

                        if not os.path.exists(os.path.dirname(destpath)):
                            try:
                                os.makedirs(os.path.dirname(destpath))
                            except OSError as exc:
                                if exc.errno != errno.EEXIST:
                                    raise

                    #if filext in supportedFiletypes:
                        print "Copying %s" %(str(file))
                        print "To %s" %(str(destpath))
                        if os.path.exists(destpath):
                            raise Exception("Destination file exists!")
                        else:
                            copyfile(sourcefile+'/'+file, destpath)

if __name__ == "__main__":
    main(sys.argv[1:])
