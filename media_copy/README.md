# Media File Copy Script

The purpose of this script is to copy and rename a file based on the type. We are handling four different cases: Movies, TV Episodes, TV Seasons, and Misc. Videos.

## Usage:
    $ python media_copy.py -[h,m,t,f,v] <source>

Movies (-m flag) are copied to /data/media/Movies and renamed "Movie Name [YEAR].ext

TV Episodes (-t flag) are copied to /data/media/TV/Show Name/Season X/SXXEXX.ext

Full TV Season (-f flag) episodes are copied sequentially to /data/media/TV/Show Name/Season X/SXXEXX.ext

Videos (-v flag) are copied to /data/media/Videos/user/defined/path/video name.ext

## Future Considerations:
* ~~Handling a dump of an entire tv series~~
* ~~Need to add handling to deal with non media files in the directory~~
* I want to rename some variables so they make more sense
