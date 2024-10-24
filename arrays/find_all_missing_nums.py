'''
Given an array nums of integers where nums[i] is the range [1,n],
return an array of all the integers in the range [1,n] that do not appear
'''

# A good rule of thumb: if the problem involves duplicates, try to use sets
def linear_all_missing_nums(nums):
    set_nums = set(nums)

    res = []

    for i in range(1, len(nums) + 1):

        if i not in set_nums:
            res.append(i)

    return res


# the optimal solution
def find_all_missing_nums(nums):
    # we would have to use a hashset data structure
    # mark existing
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])

    res = []
    for i, v in enumerate(nums):
        if v > 0:
            res.append(i + 1)
    
    return res

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(linear_all_missing_nums(nums))
    print(find_all_missing_nums(nums))