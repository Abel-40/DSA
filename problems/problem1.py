# ************************************first and last occurence of number in array**********

def first_last_occurrence(arr,target):
  no_occurrence = set()
  def left_side_checker():
    low,high= 0, len(arr) - 1
    first = -1
    nonlocal no_occurrence 
    while low <= high:
      mid = (low + high)//2
      if arr[mid] == target:
        first = mid
        no_occurrence.add(mid)
        high = mid - 1
      elif arr[mid] < target:
        low  = mid + 1
      else:
        high = mid - 1
    return first
  
  def right_side_checker():
    nonlocal no_occurrence
    low,high = 0,len(arr) - 1
    last = -1
    while low <= high:
      mid = (low + high)//2
      if arr[mid]== target:
        last = mid
        low = mid + 1
        no_occurrence.add(mid)
      elif arr[mid] < target:
        low = mid + 1
      else:
        high = mid - 1
    return last
  print(no_occurrence)
  return [left_side_checker(), right_side_checker(),len(no_occurrence)]


arr = [ 1,2,3,4,5,5,5,5,5,9]

print(first_last_occurrence(arr,5))
      
def number_of_occurrences(arr,target):
  low,high = 0,len(arr) - 1
  first = -1
  occurence = 0
  while low <= high:
    mid = (low + high)//2
    print(f"low: {low}  high: {high}")
    print(f"mid value: {mid}")
    print(f"array of mid before the condition {arr[mid]}")
    if arr[mid]== target:
      print(f"array of mid after the condition {arr[mid]}")
      first = mid
      occurence +=1
      low = mid + 1
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return [first,occurence]
  
