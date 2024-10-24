# 371 Sum of Two Integers
# Given two integers a and b, return the sum of the two integers without using '+' and '-'.
def sum_of_ints(a, b):
    # ITS XOR BRUH
    while b != 0:
        carry = a & b

        a = a ^ b

        b = carry << 1
        
    return a

if __name__ == "__main__":
    print(sum_of_ints(2, 3))