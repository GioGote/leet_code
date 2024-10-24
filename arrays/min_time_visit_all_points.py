'''
1266. Minimum Time Visiting All Points
On a 2D plane, there are n points with integer coordinates 
points[i] = [xi, yi]. Return the minimum time in seconds to 
visit all the points in the order given by points.
'''

# Solution: if the next node is +10x and -5y away, its going to take
# exactly 10 steps, because you can only move 1x at a time and the 
# difference in y us made up by diagonal moves during the process
# of overcoming the ifference in x. O(n)

def min_time_to_visit(points):
    res = 0
    x1, y1 = points.pop()
    while points:
        x2, y2 = points.pop()
        res += max(abs(y2 - y1), abs(x2 - x1))
        x1, y1 = x2, y2
    
    return res

if __name__ == "__main__":
    points = [[1,1],[3,4],[-1,0]]
    print(min_time_to_visit(points))