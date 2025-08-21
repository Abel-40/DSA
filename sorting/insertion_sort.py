def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]       # The element we want to insert
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # one position to the right to make space for key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key in its correct position
        arr[j + 1] = key
    
    return arr
