def bubble_sort_descending(arr):
  high = len(arr)
  while high > 0:
    for i in range(1,high):
      if arr[i] > arr[i-1]:
        arr[i-1],arr[i] = arr[i],arr[i-1]
    high -=1
    
arr = [4,6,7,4,6,3,9,10]
bubble_sort_descending(arr)
# print(arr)

def merge_helper(arr1,arr2):
  i,j=0,0
  result = []
  while i < len(arr1) and j < len(arr2):
    if arr2[j] > arr1[i]:
      result.append(arr2[j])
      j+=1
    else:
      result.append(arr1[i])
      i+=1
  result.extend(arr2[j:])
  result.extend(arr1[i:])
  return result
  
  
  
def merge_sort_descending(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr)//2
  left_arr = arr[:mid]
  right_arr =arr[mid:]
  new_left = merge_sort_descending(left_arr)
  new_right = merge_sort_descending(right_arr)
  
  return merge_helper(new_left,new_right)

def merge_for_strings(string_array):
  if len(string_array) == 1:
    return string_array
  mid = len(string_array)//2
  left_half = string_array[:mid]
  right_half = string_array[mid:]
  new_left_half = merge_for_strings(left_half)
  new_right_half = merge_for_strings(right_half)
  return merge_helper(new_left_half,new_right_half)

arr2 = ["abel","addis","abrham","abenzer"]
# print(merge_for_strings(arr2))


def bubble_no_of_swap(arr):
  end = len(arr)
  no_of_swap = 0
  while end > 0:
    for i in range(1,end):
      if arr[i -1] > arr[i]:
        arr[i],arr[i-1] = arr[i-1],arr[i]
        no_of_swap +=1
    end -= 1
  return no_of_swap

arr3 = [4,3, 2, 1]
# print(bubble_no_of_swap(arr3))

def k_th_smallest(arr, k):
    n = len(arr)
    for pass_num in range(k):
        for i in range(1, n - pass_num):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr[k-1]

  
arr4 = [6,5,4,3,2,1]
k_th_smallest(arr4,2)
# print(arr4)