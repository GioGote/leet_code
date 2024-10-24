# Given an array nums containing n distinct numbers in the range [0,n],
# return the only number in the range that is missing from the array

# input: nums = [3,0,1]
# output: 2

# best to use enumeration for this:
# enumeration example:

# O(n log n) Solution
def missing_number(nums):

    # first lets sort this bitch
    nums.sort()
    for i, v in enumerate(nums):
        if (i != v):
            return v - 1
        
        if v == len(nums) - 1:
            return v + 1
        
# O(n) Solution: Iterate through list and sum
def linear_missing_number(nums):
    return sum(range(len(nums) + 1)) - sum(nums)

    '''
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum
    '''

if __name__ == "__main__":

    fruits = ["apple", "banana", "orange"]

    for index, value in enumerate(fruits):
        print(index, value)

    '''
    0 apple
    1 banana
    2 orange
    '''
    nums = [3,0,1]
    print(missing_number(nums))
    print(linear_missing_number(nums))