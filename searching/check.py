def merge(left,right):
  result = []
  i,j=0,0
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
  if len(arr) <= 1:
    return arr
  mid = len(arr)//2
  
  left_arr = arr[:mid]
  right_arr = arr[mid:]
  left_sorted = merge_sort(left_arr)
  right_sorted = merge_sort(right_arr)
  
  return merge(left_sorted,right_sorted)

arr = [45,6,77,99,3,6,1,44]
  
# print(merge([2,3],[4,6]))
print(f"merge_sort: {merge_sort(arr)}")



def bubble_sort(arr):
  swapping = True
  end = len(arr)
  while swapping:
    swapping = False
    for i in range(1,end):
      if arr[i-1] > arr[i]:
        temp = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = temp
        swapping = True
    end -= 1
  return arr

print(f"bubble_sort: {bubble_sort(arr)}")
   
   
   
arr2 = [3,5,7,8,98,100]   
def binary_search(arr,target):
  low,high = 0,len(arr)-1
  occurence = -1
  while low <= high:
    mid = (low + high)//2
    if target == arr[high]:
      return occurence
    elif arr[mid] > target:
      high = mid - 1
      occurence =  arr[mid]
    else:
      low = mid + 1
  return occurence

print(f"binary_search: {binary_search(arr2,1)}")
