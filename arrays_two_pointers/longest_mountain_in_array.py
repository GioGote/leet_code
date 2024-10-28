'''
You may recall that an array arr is a mountain array if and only if:

    arr.length >= 3
    There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array arr, return the length of the longest subarray, which is a mountain. 
Return 0 if there is no mountain subarray.
'''

def longest_mountain(arr):

    n = len(arr)

    left = 0
    result = 0

    while left < n:
        # find the starting point of increasing sequence
        while left < n - 1 and arr[left] >= arr[left + 1]:
            left += 1

        # now move the right pointer
        right = left + 1

        # find the end of increasing sequence
        while right < n - 1 and arr[right] < arr[right + 1]:
            right += 1

        # try to find decreasing sequence
        while right < n - 1 and arr[right] > arr[right + 1]:
            right += 1
            result = max(result, right - left + 1)
        
        left = right

    return result