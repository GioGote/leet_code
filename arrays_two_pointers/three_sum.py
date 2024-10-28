'''
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

def three_sum(nums):
    triplets = []

    nums.sort()

    # first loop through considering i
    for i, val in enumerate(nums):

        if (i > 0) & (val == nums[i - 1]):
            continue

        left = (i + 1)
        right = (len(nums) - 1)

        while left < right:

            current_sum = val + nums[left] + nums[right]

            if current_sum > 0:
                right -= 1

            elif current_sum < 0:
                left += 1

            else:
                triplets.append([val, nums[left], nums[right]])

                left += 1

                while (left < right) & (nums[left] == nums[left - 1]):
                    left += 1

    return triplets