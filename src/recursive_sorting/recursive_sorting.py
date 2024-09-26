# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # TO-DO
    merged_arr = []

    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            value = arrA.pop(0)
        else:
            value = arrB.pop(0)
        merged_arr.append(value)

    merged_arr += arrA
    merged_arr += arrB

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    halfway_index = len(arr) // 2

    left = merge_sort(arr[:halfway_index])
    right = merge_sort(arr[halfway_index:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
