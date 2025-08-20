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