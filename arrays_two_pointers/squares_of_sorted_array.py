'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
'''

import collections


def square_sort_array(nums):
    # my attempt:
    '''
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    '''
    # YOU FUCKING IDIOT, SQUARING A NEG NUMBER MAKES IT POSITIVE

    #nums.sort()

    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

    nums.sort()
    
    return nums

# absolute and merge
def sorted_squares(nums):
    answer = collections.deque()
    l, r = 0, len(nums) - 1

    while l <= r:
        left_value, right_value = abs(nums[l]), abs(nums[r])
        if left_value > right_value:
            answer.appendleft(left_value * left_value)
            l += 1
        else:
            answer.appendleft(right_value * right_value)
            r -= 1

    return list(answer)

if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    # print(square_sort_array(nums))
    print(sorted_squares(nums))