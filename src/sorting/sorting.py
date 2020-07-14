# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    lenA, lenB = len(arrA), len(arrB)
 # Initialize a list large enough to hold both sorted lists
    merged_arr = [0] * (lenA + lenB)
  # Build a merged list, stepping through arrA and arrB
  # and adding the lowest values in order, until the end
  # of either list is reached
    indexA = indexB = merged_index = 0
    while indexA < lenA and indexB < lenB:
        if arrA[indexA] <= arrB[indexB]:
            merged_arr[merged_index] = arrA[indexA]
            indexA += 1
        else:
            merged_arr[merged_index] = arrB[indexB]
            indexB += 1
        merged_index += 1

    # Add the remaining elements from whichever list hadn't
    # been stepped through completely
    if indexA < lenA:
        merged_arr[merged_index:] = arrA[indexA:]
    else:
        merged_arr[merged_index:] = arrB[indexB:]

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    lenArr = len(arr)
    # While the data set contains more than one item, split it in half
    # Once down to a single element, you have also *sorted* that element
    if lenArr > 1:
        half = lenArr // 2
        # Start merging sorted lists together into larger, sorted sets
        return merge(merge_sort(arr[:half]), merge_sort(arr[half:lenArr]))
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
