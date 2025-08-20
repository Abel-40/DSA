def bubble_sort(arr):
  end = len(arr)
  while end > 0:
    for i in range(1,end):
      if arr[i - 1] > arr[i]:
        arr[i-1],arr[i] = arr[i],arr[i-1]
    end -=1
 

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


    



