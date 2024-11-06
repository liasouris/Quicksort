def quicksort_last_pivot(arr):
    def _quicksort(subarray, pivot_count):
        if len(subarray) < 2:
            return subarray, pivot_count
        
        # Choose the pivot as the last element
        pivot = subarray[-1]
        pivot_count += 1

        # Partitioning
        left = [x for x in subarray[:-1] if x < pivot]
        right = [x for x in subarray[:-1] if x >= pivot]

        # Recursive calls to sort both partitions
        sorted_left, pivot_count = _quicksort(left, pivot_count)
        sorted_right, pivot_count = _quicksort(right, pivot_count)

        return sorted_left + [pivot] + sorted_right, pivot_count

    sorted_array, pivot_count = _quicksort(arr, 0)
    return sorted_array, pivot_count

# Input array
array = [14, 1, 2, 6, 11, 8, 5, 9, 4, 3, 10, 7, 12, 13]

# Perform quicksort with the last element as pivot
sorted_array, pivot_count = quicksort_last_pivot(array)

print("Sorted array with last element as pivot:", sorted_array)
print("Number of pivots used:", pivot_count)
