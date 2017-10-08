
def partition(list_val, pivot_index=None):
    """Function to pivot around a given index. Example use is in quick sort"""
    """Returns index of pivot"""
    list_size = len(list_val)
    if list_size:
        pivot_index = pivot_index or list_size - 1
        pivot = list_val[pivot_index]
        # swap pivot with last element
        list_val[pivot_index], list_val[list_size - 1] = list_val[list_size - 1], list_val[pivot_index]
        # i is boundary of partition with smaller elements; j is boundary of partition with higher elements.
        # in between i and j is the working area
        i, j = 0, list_size - 1
        while j > i:
            if list_val[j - 1] > pivot:
                list_val[j] = list_val[j - 1]
                j = j - 1
            else:
                list_val[i], list_val[j - 1] = list_val[j - 1], list_val[i]
                i = i + 1
        list_val[j] = pivot
        return j
    else:
        return None