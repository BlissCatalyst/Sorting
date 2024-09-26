# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:  # and j >= cur_index:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    iterate = True
    while iterate == True:
        if len(arr) <= 0:
            iterate = False
        changed = False
        for i in range(0, len(arr) - 1):
            if i == (len(arr) - 2) and changed == False:
                iterate = False
            elif arr[i] > arr[i + 1]:
                switch = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = switch
                changed = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
