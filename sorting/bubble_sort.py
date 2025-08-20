def bubble_sort(arr):
  high = len(arr)
  while high > 0:
    for i in range(1,high):
      if arr[i-1] > arr[i]:
        arr[i-1],arr[i] = arr[i],arr[i-1]
    high -= 1

arr = [23,2,554,233,2323,522,2,1,55]

bubble_sort(arr)
print(arr)


