def bubble_sort(array):
    n = len(array)
    for i in range(n):
        print(array)
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


array = [64, 34, 25, 12, 22, 11, 90]#
sorted_array = bubble_sort(array)
print("Sorted array is:", sorted_array)