def selection_sort(array):
    n = len(array)
    for i in range(n):
        print(array)
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print("Sorted array is:", sorted_array) 