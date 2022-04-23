# selection sort
# find the smaller element and then swap it in front using a moving pointer (i)
# O(n^2)

def selection_sort(arr):
    i = 0
    while i < len(arr):  # while the entire list is not through
        lowest = i  # set initial lowest value to first index[0]
        j = i + 1  # set j pointer to start 1 index ahead of i
        while j < len(arr):  # j pointer must go through all the elements ahead of i
            if arr[i] > arr[j]:  # if the current element is smaller than the lowest (i)
                lowest = j  # update the new lowest
                arr[i], arr[j] = arr[j], arr[i]  # swap the elements
            j += 1  # increment to continue until the loop is over
        i += 1

    return arr
