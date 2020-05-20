# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[i+j] = arrA[i]
            i += 1
        else:
            merged_arr[i+j] = arrB[j]
            j += 1

    while i < len(arrA):
        merged_arr[i+j] = arrA[i]
        i += 1
    while j < len(arrB):
        merged_arr[i+j] = arrB[j]
        j += 1

    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # check if array is empty (already sorted)
    if len(arr) <= 1:
        return arr

    # Get mid index
    mid = len(arr) // 2
    # recursively sort left & right halve
    l, r = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    # merge left & right
    arr = merge(l, r)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    i = start
    j = mid + 1

    # check if merge already sorted
    if arr[mid] <= arr[j]:
        return arr

    while i <= mid and j <= end:
        # print(arr)
        # check if element i is in right place
        if arr[i] < arr[j]:
            i += 1
        else:
            j_index, j_value = j, arr[j]

            # shift items between elements i & j to the right
            while j_index > i:
                arr[j_index] = arr[j_index - 1]
                j_index -= 1

            arr[i] = j_value

            # update pointers
            i += 1
            j += 1
            mid += 1

    return arr




def merge_sort_in_place(arr, l, r):
    # check if array is empty
    if (r - l) < 1:
        return arr

    # Get mid index
    mid = (l + r) // 2

    # recursively sort left & right halve
    merge_sort_in_place(arr, l, mid)
    merge_sort_in_place(arr, mid + 1, r)

    # merge left & right
    merge_in_place(arr, l, mid, r)

    return arr



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
