'''
1365 How many numbers are smalller than the current number
given the array nums, for each nums[i] find out how many numbers in the array
are smaller than it. That is, for each nums[i]
'''

# could be better time complexity
def smaller_nums_than_current(nums):
    res = []

    for i in range(len(nums)):
        res.append(0)
        counter = 0 # initialize a new counter for every loop
        for j in range(len(nums)): # DONT NEED TO DO i + 1 SINCE GOING THROUGH REST OF LIST
            if nums[i] > nums[j]:
                counter += 1
        res[i] = res[i] + counter
    
    return res

# O(n log n) solution:
def better_solution(nums):
    # the idea here is to sort the array first
    temp = sorted((nums))

    hash_map = {}
    # hash_map = {1:0, 2:1, 3:3, 8:4}
    for i, v in enumerate(temp):
        if v not in hash_map:
            hash_map[v] = i

    res = []
    # res = [4,0,1,1,3]
    for i in nums:
        res.append(hash_map[i]) # checking dictionary location from sorting array

    return res

if __name__ == "__main__":
    nums = [8,1,2,2,3]
    print(smaller_nums_than_current(nums))
    print(better_solution(nums))