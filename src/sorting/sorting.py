# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = j = k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            i = i + 1
        else:
            merged_arr[k] = arrB[j]
            j = j + 1
        k = k + 1

    # Add the remaining elements from whichever list hadn't
    # been stepped through completely
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i = i + 1
        k = k + 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j = j+1
        k = k+1
    print("Merging ", arrA, arrB)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # While the data set contains more than one item, split it in half
    # Once down to a single element, you have also *sorted* that element
    if len(arr) > 1:
        half = len(arr) // 2
        # Start merging sorted lists together into larger, sorted sets
        return merge(merge_sort(arr[:half]), merge_sort(arr[half:len(arr)]))
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
