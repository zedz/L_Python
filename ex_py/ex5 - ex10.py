#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Jamie Zhang on 2012-02-16.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	pass


if __name__ == '__main__':
	main()

	print "<<< ex 5 >>>"
	my_name = 'Zed A. Shaw'
	my_age = 35 # not a lie
	my_height = 74 # inches
	my_weight = 180 # lbs
	my_eyes = 'Blue'
	my_teeth = 'White'
	my_hair = 'Brown'

	print "Let's talk about %s." % my_name
	print "He's %s inches tall." % my_height
	print "He's %s pounds heavy." % my_weight
	print "Actually that's not too heavy."
	print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
	print "His teeth are usually %s depending on the coffee." % my_teeth

	# this line is tricky, try to get it exactly right
	print "If I add %s, %s, and %s I get %s." % (
	    my_age, my_height, my_weight, my_age + my_height + my_weight)
	print

	print "<<< ex 6 >>>"
	x = "There are %d types of people." % 10
	binary = "binary"
	do_not = "don't"
	y = "Those who know %s and those who %s." % (binary, do_not)

	print x
	print y

	print "I said: %r." % x
	print "I also said: '%s'." % y

	hilarious = False
	joke_evaluation = "Isn't that joke so funny?! %s"

	print joke_evaluation % hilarious

	w = "This is the left side of..."
	e = "a string with a right side."

	print w + e
	print 

	print "<<< ex 7 >>>"
	print "Mary had a little lamb."
	print "Its fleece was white as %s." % 'snow'
	print "And everywhere that Mary went."
	print "." * 10  # what'd that do?

	end1 = "C"
	end2 = "h"
	end3 = "e"
	end4 = "e"
	end5 = "s"
	end6 = "e"
	end7 = "B"
	end8 = "u"
	end9 = "r"
	end10 = "g"
	end11 = "e"
	end12 = "r"

	# watch that comma at the end.  try removing it to see what happens
	print end1 + end2 + end3 + end4 + end5 + end6,
	print end7 + end8 + end9 + end10 + end11 + end12
	print "%s%s%s%s%s%s%s%s%s%s%s%s%s" % (end1, end2, end3, end4, end5, end6, " " , end7, end8, end9, end10, end11, end12)
	print

	print "<<< ex 8 >>>"
	formatter = "%r %r %r %r"

	print formatter % (1, 2, 3, 4)
	print formatter % ("one", "two", "three", "four")
	print formatter % (True, False, False, True)
	print formatter % (formatter, formatter, formatter, formatter)
	print formatter % (
	    "I had this thing.",
	    "That you could type up right.",
	    "But it didn't sing.",  #why输出的是???双引号???
	    "So I said goodnight."
	)
	
	formatter2 = "%s %s %s.  %s %s %s."
	formatter3 = "%s%s%s%s%s%s%s"
	a ="Jamie"
	b ="Echo"
	v ="love"
#	print formatter %(a,b,v)  # warning that less argument
#	print formatter %(a,b,v,b,v,a) #'not all arguments converted during string formatting'
	print formatter2 %(a,v,b,b,v,a)
#	print formatter2 %(a,b,v," ",b,v,a) #'not all arguments converted during string formatting'
	print formatter3 %(a,v,b," ",b,v,a) 
	print
		
	print "<<< ex 9 >>>"
	# Here's some new strange stuff, remember type it exactly.

	days = "Mon Tue Wed Thu Fri Sat Sun"
	months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
	months3 = "\tJan\n\tFeb\n\tMar\n\tApr\n\tMay\n\tJun\n\tJul\t\nAug" #\t必须放在\n的后面

	print "Here are the days: ", days
	print "Here are the months: ", months

	print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""", "Jan" #为啥这个逗号没用了(Jan没有在同一排开始)，  所以三引号后的逗号总失效？
	print "a", "Jan"
	print months3
	print 
	
	print "<<< ex 10 >>>"
	tabby_cat = "\tI'm tabbed in."
	persian_cat = "I'm split\non a line."
	backslash_cat = "I'm \\ a \\ cat."

	fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip	\n\t* Grass 
""" #\n\t放在同一排的输出效果不一样  且在三引号中的缩进最好只用\t来表示以免产生错误

	print tabby_cat
	print persian_cat
	print backslash_cat
	print fat_cat
	print
	

	

