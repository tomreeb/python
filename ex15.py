from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "\nThis script, %s, allows you to read contents of a file" % script
print "Type the filename:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()