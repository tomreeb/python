#!/usr/local/bin/python
import os
import sys 
import readline
import glob

class tabCompleter(object):

    def pathCompleter(self,text,state):
        """ 
        This is the tab completer for systems paths.
        Only tested on *nix systems
        """
        line   = readline.get_line_buffer().split()

        return [x for x in glob.glob(text+'*')][state]

if __name__=="__main__":
    t = tabCompleter()

    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")

    readline.set_completer(t.pathCompleter)
    ans = raw_input("What file do you want? ")
    print ans