# runs in linear time
def max_unsorted(arr):
    max_element = arr[0]

    for i in arr:
        if i > max_element:
            max_element = i

    return max_element

print(max_unsorted([556,11,23,167,2,9]))