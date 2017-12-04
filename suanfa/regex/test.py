import re
print re.match('123','www.xpyou.cn')

line = "Cats are smarter than dogs"

robj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if robj:
    print 'group:',robj.group()
    print 'group1:',robj.group(1)
    print 'group2:', robj.group(2)
else:
    print 'no match'


