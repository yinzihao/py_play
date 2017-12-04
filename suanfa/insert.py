arr = [2,4,6,2,3,1,0]
j =2
for j in range(len(arr)):
    key = arr[j]
    i =j -1
    while i>0 and arr[i] > key:
        arr[i+1] = arr[i]
        i = i-1
    arr[i+1]  =key

print arr



