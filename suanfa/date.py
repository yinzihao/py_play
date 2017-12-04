import time
ticks = time.time()
print "now time:",time.strftime("%Y-%m-%d %H:%M",time.localtime())

def test(test):
    print test
    return test
test(123);
