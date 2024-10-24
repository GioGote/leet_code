# This will be an example of a two pointer solution from the Leetcode 42 problem of "Trapping Rain Water"
# May God have mercy on my soul

# Given 'n' non-negative integers representing an elevation map where the width of each bar 1,
# compute how much water it can trap after raining.

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# min(l,r) - h[i]

def trapping_rain_water(height):
    if not height: return 0

    l, r = 0, len(height) - 1
    
    l_max, r_max = height[l], height[r]

    res = 0

    while l < r:
        if l_max < r_max:
            l += 1
            l_max = max(l_max, height[l])
            res += l_max - height[l]
        else:
            r -= 1
            r_max = max(r_max, height[r])
            res += r_max - height[r]
    
    return res

print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))