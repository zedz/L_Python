from sys import argv

f = 'ex15.txt'
txt = open(f)

print "Here's your file %r:" % f
print txt.read()

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

#txt_again = open(file_again)

#print txt_again.read()

print open(file_again).read()

#################################### argv problem
#
#from sys import argv
##导入argv模块
#
#script, filename = argv
##给argv后的参数进行定义，使其可以在往后的脚本中被调用
#
#txt = open(filename)
##将txt赋值为打开filename文件
#
#print "Here's your file %r:" % filename
##输出文件名filename
#print txt.read()
##打印从filename中读出的内容
#
#print "I'll also ask you to type it again:"
#file_again = raw_input("> ")
##请求输入文件名
#
#txt_again = open(file_again)
##打开刚刚输入的文件名
#
#print txt_again.read()
##读出打开的文件的内容
#
########################################################