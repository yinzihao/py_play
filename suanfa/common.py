def post():
    return 200

def py_read_file(path,length):
    fo = open(path,'r+')
    str = fo.read(length)
    fo.close()
    return str
