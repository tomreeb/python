# Media File Copy Script
By: Tom Reeb, March 22nd 2016

The purpose of this script is to copy and rename a file based on the type. We are handling three different types of files: Movies, TV Episodes, and Misc. Videos.

## Usage: 
    $ python media_copy.py -[h,m,t,v] <sourcefile>

Movies (-m flag) are copied to /data/media/Movies and renamed "Movie Name [YEAR].ext

TV Episodes (-t flag) are copied to /data/media/TV/Show Name/Season X/SXXEXX.ext

Videos (-v flag) are copied to /data/media/Videos/user/defined/path/video name.ext

Future consideration will be handling a dump of an entire tv series