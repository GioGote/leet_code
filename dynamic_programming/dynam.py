# 70. Climbing Stairs
# You are climbing a staircase. it takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. in how many distinct way can you climb to the top?

def climb_stairs(int):
    one, two = 1, 1

    for i in range(int - 1):
        temp = one
        one = one + two
        two = temp
    
    return one

if __name__ == "__main__":
    print(climb_stairs(10))