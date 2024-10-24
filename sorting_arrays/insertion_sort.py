def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
if __name__ == "__main__":
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = insertion_sort(unsorted_array)
    print(sorted_array)