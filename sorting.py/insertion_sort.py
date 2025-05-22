def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        print(array)
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

array = [5, 2, 9, 1, 5, 6]

insertion_sort(array)
print("Sorted array is:", array)