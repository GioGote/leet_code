def contains_dup_ii(nums, k):
    seen = set()
    for i, val in enumerate(nums):
        if val in seen:
            return True
        seen.add(val)
        if len(seen) > k:
            seen.remove(nums[i - k])
    
    return False