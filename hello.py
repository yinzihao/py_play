arr = [1,4,7,9,2]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] > arr[j] :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print arr
