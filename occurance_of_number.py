def occurance_1stNum(arr,start,end,key):
    res1 = -1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            res1 = mid
            end = mid-1

        elif key < arr[mid]:
            end = mid-1
        elif key > arr[mid]:
            start = mid+1
    return res1
    return -1

def occurance_lastNum(arr,start,end,key):
    res_last = -1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            res_last = mid
            start = mid+1

        elif key < arr[mid]:
            end = mid-1
        elif key > arr[mid]:
            start = mid+1
    return res_last
    return -1

arr = [3,5,10,10,10,12,15]
n = len(arr)
key = 10
index1 = occurance_1stNum(arr,0,n-1,key)
index_last = occurance_lastNum(arr,0,n-1,key)
#occuranceNum(arr,0,n-1,key)
if index1 == -1 or index_last == -1:
    print("no such element")
else:
    print(f"The first occurance of {key} is at {index1} index")
    print(f"The first occurance of {key} is at {index_last} index")
print(f"{key} occured {(index_last-index1)+1} times in the given array.")

print("Supriya added her changes.")
print("Amit_2 added changes.")
