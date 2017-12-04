import common
print common.post()


#file
fo = open('1.txt','wb')
print "file name:",fo.name
#fo.close()
print "is close:",fo.closed

fo.write("hello python\n")

