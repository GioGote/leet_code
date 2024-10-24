# NUMBAH ONE BAYBEEEEEE: Two Sum
def two_sum(nums, target):
    prevMap = {} # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return

if __name__ == "__mid__":
    print(two_sum([1,2,3,4,5,6,7,8,9], 7))