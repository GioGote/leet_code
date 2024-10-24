# two sum baybee
'''
Given an array of integers nums and an integer, return indices of
the two numbers such that they add up to target
'''
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j] # RETURN INDICES DUMMY

# linear solution:
def linear_two_sum(nums, target):
    # create a hashmap/dictionary
    # fill hashmap while iterating through array
    hash_map = {}

    for i, v in enumerate(nums):
        diff = target - v
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[v] = i

if __name__ == "__main__":
    nums = [2,7,11,15]
    print(two_sum(nums, 9))
    print(linear_two_sum(nums, 9))