def merge_sort(arr):
    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]


    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result





arr = [23,2,554,233,2323,522,2,1,55]
arr2 = ["abel","addis","abrham","abenzer"]
print(merge_sort(arr2))




    
  