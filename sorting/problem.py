def bubble_sort(arr):
  end = len(arr)
  swapping = True
  while swapping:
    swapping = False
    for i in range(1,end):
      if arr[i - 1] > arr[i]:
        temp = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = temp
        swapping = True
    end -=1
  return arr

def merge(left,right):
  i,j = 0,0
  result = []
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i +=1
    else:
      result.append(right[j])
      j +=1
  result.extend(left[i:])
  result.extend(right[j:])
  return result
def merge_sort(arr):
  if len(arr) == 1:
    return arr
  
  mid = len(arr) //2
  left_array = arr[:mid]
  right_array = arr[mid :]
  new_left = merge_sort(left_array)
  new_right = merge_sort(right_array)
  return merge(new_left,new_right)


    

arr = [8,9,7,5,4,6,2,10]



def binary_search(arr,target):
  sorted_arr = merge_sort(arr)
  low,high = 0,len(sorted_arr) - 1
  index_of_target = -1
  while low <= high:
    mid = (low + high) // 2
    if sorted_arr[mid] == target:
      index_of_target = mid
      break
    elif sorted_arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return index_of_target
   

# print(binary_search(arr,7))


def square_root(n):
  low = 1
  high = n
  ans = -1
  while low <= high:
    mid = (low + high) //2
    if mid * mid == n:
      ans = mid
      break
    elif mid * mid < n:
      ans = mid
      low = mid + 1
      
    else:
      high = mid - 1
  return ans
print(square_root(37))