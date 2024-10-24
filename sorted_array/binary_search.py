# Search through an already sorted sequence to find if the item we are looking for is there

# [1,2,3,4,5,6,7] target is the number 7
# search == midpoint = return position

def binary_search(sequence, target):
    left = 0 # initialize left position
    right = len(sequence) - 1 # initialize right position

    while left <= right: # Keep in loop that only breaks when target is found or list is exhausted
        mid = (left + right) // 2

        if sequence[mid] < target:
            left = mid + 1
        
        elif sequence[mid] > target:
            right = mid - 1
        
        else:
            return "Your target value is at index: " + str(mid)
        
    return -1

# LeetCode 367. Valid Perfect Square
# Given a positive integer num, write a function which returns True if num is a perfect square else False
# DO NOT use any built-in library functioon such as sqrt

def is_perfect_square(num):
    l, r = 1, num

    while l <= r:
        mid = (l + r) // 2
        if mid * mid > num:
            r = mid - 1
        elif mid * mid < num:
            l = mid + 1
        else:
            return True
    
    return False

# 441. Arragning Coins
# you have n coins and you want to build a staircase with these coins. The staircase consists
# of k rows where the i^th row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

# We gotta use Gauss's formula
def arrange_coins(num):
    l, r = 0, num
    res = 0 

    while l <= r:
        mid = (l + r) // 2

        coins = (mid / 2) * (mid + 1)
        if coins > num:
            r = mid - 1
        else:
            l = mid + 1
            res = max(mid, res)
    
    return res

# Leetcode 374 Guessing Game

def guess_game(num):
    l, r = 0, num

    while l <= r:
        mid = (l + r) // 2
        if mid == num:
            return mid
        elif mid > num:
            r = mid - 1
        else:
            l = mid + 1

# 74. Search a 2D Matrix
# Write an eddicient algorithm that searches for a value in an m x n matrix. 
# This matric has the following properties:
#   Integers in each row are sorted from left to right.
#   The first integer of each row is greater than the last integer of the previous row.

# binary search to figure out location AND row to search
def search_matrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    # second portion of binary loop
    if not (top <= bot):
        return False
    
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
        
    return False

# leetcode 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# if not, return the index where if would be if it were inserted in order
def search_insert(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return l

if __name__ == "__main__":

    print(binary_search([1,2,3,4,5,6,7,8,9], 3))
    print(is_perfect_square(15))
    print(arrange_coins(10))
    print(guess_game(100))
    print(search_insert([1,2,4,5,6,7], 3))