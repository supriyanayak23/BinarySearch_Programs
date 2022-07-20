def binarySearch(arr,start, end, key):
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid+1
        elif arr[mid] > key:
            end = mid-1
    return -1

arr = [-4,-1,0,1,2,3,4,5,6,7,8]
n = len(arr)
key = 7
index = binarySearch(arr,0,n-1,key)
if index == -1:
    print("no such element")
else:
    print(f"The value {key} is at {index+1} position")


Print("Amit added his changes")
