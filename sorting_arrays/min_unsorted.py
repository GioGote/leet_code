def min_unsorted(arr):

    min_element = arr[0]
    for i in arr:
        if i < min_element:
            min_element = i
    
    return min_element

if __name__ == "__main__":

    print(min_unsorted([22,4,77,89,100,1]))