def num_rotation_array(arr,n):
    start = 0
    end = n-1
    while start <= end:
        mid = start + ((end-start)//2)
        prev = ((mid-1) + n) % n
        next = (mid+1) % n
        if ((arr[mid] < arr[prev]) and (arr[mid] < arr[next])):
            return (n - mid)
        if arr[mid] <= arr[end]:
            end = mid-1
        elif arr[mid] >= arr[start]:
            start = mid+1
    return -1

#arr = [2,3,1]
#arr = [11,15,16,18,2,4,5,6]
arr = [6,11,15,16,18,2,4,5]

n = len(arr)
num = num_rotation_array(arr,n)
if num == -1:
    print("there is no rotation")
else:
    print("number of rotation in the array:", num)




