# 125. Valid Palindrome String
def is_plaindrome(s):
    # Convert to lowercase and filter out non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum()) 

    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        
        l += 1
        r -= 1
    
    return True

if __name__ == "__main__":

    print(is_plaindrome("A man, a plan, a canal: Panama"))
    print(is_plaindrome("race a car"))