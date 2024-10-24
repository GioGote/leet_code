# 242. Valid Anagram

# hashmap solution
def count_occurence(s, t):
    if len(s) != len(t): return False

    # initialize hashmaps
    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)

    for char in count_s:
        if count_s[char] != count_t.get(char, 0):
            return False
        
    return True

# solution with O(1) memory
# sorted order should become the exact same string
def sorted_occurence(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    print(count_occurence("anagram", "nagaram"))
    print(sorted_occurence("anagram", "nagaram"))