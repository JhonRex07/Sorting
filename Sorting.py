# Data Structures and Algorithms
# Programmed by Jhon Rex B. Jusayan

def selection_sort(array):
    for i in range(0, len(array) - 1):
        index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index]:
                index = j

        (array[i], array[index]) = (array[index], array[i])

array = [30, 6, 92, 72, 39, 97, 63, 87, 66, 57]
selection_sort(array)
print("Selection Sort:", array)

def bubble_sort(array):
    index = len(array) - 1
    sort = False
    
    while not sort:
        sort = True
        for i in range(0, index):
            if array[i] > array[i + 1]:
                sort = False
                array[i], array[i + 1] = array[i + 1], array[i]
    return array

array = [30, 6, 92, 72, 39, 97, 63, 87, 66, 57]
bubble_sort(array)
print("Bubble Sort:   ", array)

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1

array = [30, 6, 92, 72, 39, 97, 63, 87, 66, 57]
insertion_sort(array)
print("Insertion Sort:", array)

def merge_sort(array):
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
                k += 1
            else:
                array[k] = right_array[j]
                j += 1
                k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

array = [30, 6, 92, 72, 39, 97, 63, 87, 66, 57]
merge_sort(array)
print("Merge Sort:    ",array)

def quicksort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quicksort(array, left, pivot - 1)
        quicksort(array, pivot + 1, right)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):

        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

array = [30, 6, 92, 72, 39, 97, 63, 87, 66, 57]
quicksort(array, 0, len(array) - 1)
print("Quicksort:     ", array)

