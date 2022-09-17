def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheeses!" % cheese_count
    print "you have %d boxes of crackers" % boxes_of_crackers
    print "Get a blanket. \n"

print " we can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackeers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackeers)

print "we can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 5)