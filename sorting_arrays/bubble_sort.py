def bubble_sort(nums):
    
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

if __name__ == "__main__":

    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(unsorted_array)
    print(sorted_array)