def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# We are asking the user but raw_input is a string, we need an int
# The first input is converted to an int right away
# The second takes input as a string and converts it after

print "Let me ask you some stuff:"
cheese = int(raw_input("How much cheese? "))

crackers = raw_input( "How many crackers? ")
crackersint = int(crackers)

cheese_and_crackers(cheese, crackersint)