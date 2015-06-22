from sys import argv

first = raw_input("What is your first argument?")
second = raw_input("What is your second argument?")
third = raw_input("What is your third argument?")

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third