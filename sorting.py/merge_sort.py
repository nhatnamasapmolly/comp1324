def merge_sort(array, start, end):
    if start < end:
        # Find the middle point
        mid = (start + end) // 2

        # Recursively sort the first and second halves
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)

        # Merge the sorted halves
        merge(array, start, mid, end)

def merge(array, start, mid, end):
    # Create temporary arrays to hold the two halves
    left = array[start:mid + 1]
    right = array[mid + 1:end + 1]

    # Initialize pointers for left, right, and the main array
    i = 0  # Pointer for left array
    j = 0  # Pointer for right array
    k = start  # Pointer for the main array

    # Merge the two halves into the main array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left array
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right array
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

# Example usage
array = [38, 27, 43, 3, 9, 82, 10]
merge_sort(array, 0, len(array) - 1)
print("Sorted array is:", array)