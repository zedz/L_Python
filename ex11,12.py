print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#so, the difference between /r and /s is single quote mark? no, i think at least with some other marks differences..


age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)

#it will ask for input everytime you print, when you use this command.
#how to make inputs to be stored in variables?
