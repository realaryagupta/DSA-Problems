arr = [1, 0, 2, 1, 1, 0,2,1,2] 

low, mid = 0, 0
high = len(arr) - 1

while mid <= high:

    if arr[mid] == 0:
        arr[low] , arr[mid] = arr[mid], arr[low]
        low = low + 1
        mid = mid + 1

    elif arr[mid] == 1:
        mid = mid + 1

    else:
        arr[mid] , arr[high] = arr[high], arr[mid]
        high = high - 1 
    
print(arr)