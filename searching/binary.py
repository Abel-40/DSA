


def min_element(arr):
    intial = float('inf')
    for num  in arr:
        if num < intial:
            intial = num
    return intial


def binar_s(arr, target):
    low,high = 0,len(arr)-1
    first = -1
    while low <= high:
        median = (low + high)//2
        if arr[median]== target:
            first = median
            high = median - 1
        elif arr[median] < target:
            low = median + 1
        else:
            high = median  - 1
    return first

arr = [1, 2, 4, 5,6, 7,9]



def small_greater_of_target(arr,target):
    low,high = 0,len(arr) - 1
    first = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] > target:
            first = arr[mid]
            high = mid - 1
        else :
            low = mid + 1
    return first

print(small_greater_of_target(arr,5))

def first_last_index(arr,target):
    def left_checker():
        low,high = 0,len(arr) - 1
        first = -1
        while low <= high:
            median = (low + high)//2
            if arr[median] == target:
                first = median
                high = median - 1
            elif arr[median] < target:
                low = median + 1
            else:
                high = median - 1
        return first
    def right_checker():
        low,high = 0,len(arr) - 1
        first = -1
        while low <= high:
            median = (low+high)//2
            if arr[median] == target:
                first = median
                low = median + 1
            elif arr[median] < target:
                low = median + 1
            else:
                high = median - 1
        return first
    
    return [left_checker(),right_checker()]


arr = [1,2,3,4,5,6,6,6,7,8,9]
print(first_last_index(arr,6))