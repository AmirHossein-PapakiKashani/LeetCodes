def quick_sort(arr):
    # Create a stack to keep track of unsorted subarrays
    stack = []
    
    # Start with the entire array
    stack.append((0, len(arr) - 1))
    
    while stack:
        # Get the next subarray to sort
        low, high = stack.pop()
        
        # If subarray has 1 or 0 elements, skip
        if low >= high:
            continue
        
        # Choose pivot (here, we pick the last element)
        pivot = arr[high]
        
        # Partition the array
        i = low - 1  # Tracks the last element smaller than pivot
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap
        
        # Place pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_pos = i + 1
        
        # Push left and right partitions onto the stack
        stack.append((low, pivot_pos - 1))   # Left partition (smaller than pivot)
        stack.append((pivot_pos + 1, high))  # Right partition (larger than pivot)
    
    return arr

quick_sort([3,1,7,2,5,9,4,8])