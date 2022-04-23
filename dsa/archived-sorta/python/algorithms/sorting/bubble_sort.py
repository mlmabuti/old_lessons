def bubble_sort(arr):
    i = 0
    while i < len(arr):
        j = i+1
        while j < len(arr):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
            j += 1
        i += 1
    return arr
