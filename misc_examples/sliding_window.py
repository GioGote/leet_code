# 53. Maximum Subarray
def max_sub_array(nums):
    max_sub = nums[0]
    cur_sum = 0

    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        max_sub = max(max_sub, cur_sum)

    return max_sub

# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters

def longest_substring_without_dups(s):
    char_set = set()
    res = 0

    # left and right pointer for sliding window
    l = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r - l + 1)
    
    return res

if __name__ == "__main__":
    print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
    print(longest_substring_without_dups("abcabcbb"))