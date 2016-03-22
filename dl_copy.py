#!/usr/local/bin/python

# File copy script
#
# Purpose of this script is to copy newly downloaded TV shows to their destination
#
# Read download folder every hour for newly added files or folders.
# Determine what kind of data it is, music, movie, tv-series or other.
# Copy file, or extract if compressed, to the corresponding directory.
# Rename the newly created folder to comply with the naming scheme.

import os
import sys
import subprocess

VIDEO_FILE_TYPES = ['avi','mpg','mkv','divx','vob','mp4','m4v','MOV']
AUDIO_FILE_TYPES = ['mp3','ogg','flac','wav']
EBOOK_FILE_TYPES = ['mobi','pdf']

DOWNLOAD_DIR = '~/Movies/source/'
DESTINATION_FILE = '~/Movies/dest/{TYPE}/{FILENAME}'
MOVE_COMMAND = 'mv {SRC} {DEST}'

def main():
  for root, dir, files in os.walk(DOWNLOAD_DIR):
    for filename in files:
      try:
        fn, ext = filename.lower().split('.',1)      
      
        if ext in VIDEO_FILE_TYPES:
          file_type='video'
        elif ext in AUDIO_FILE_TYPES:
          file_type='music'
        elif ext in EBOOK_FILE_TYPES:
          file_type='ebook'
        else:
          file_type='misc'
          
        source_file = os.path.join(root, filename)
        DESTINATION_FILE.format(TYPE=file_type, FILENAME=filename)
        MOVE_COMMAND.format(SRC=source_file, DEST=DESTINATION_FILE)
          
        rtn  = subprocess.call(MOVE_COMMAND, shell=True)
      except IndexError:
        print 'File: %s - has no extension' % (file)

if __name__ == '__main__':
  main()
