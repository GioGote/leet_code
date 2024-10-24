def contains_dup(list):

    # non the most ideal solution
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return True
            
    return False

# Linear Solution:
def linear_contain_duplicate(list):

    # Use set()
    if len(set(list)) == len(list):
        return False
    else:
        return True
    
    # Sets are fast, note that an empty set cannot be created through {}
'''
def range_print(list):
    # prints out index place starting at 0
    for i in range(len(list)):
        print(i)

    # prints the length of list
    print(len(list))

    # prints out value(s) in list
    for i in list:
        print(i)
'''

if __name__ == "__main__":

    array_dup = [1,2,3,4,5,6,6]
    array_unique = [1,2,3,4,5,6]
    print(contains_dup(array_dup))
    print(contains_dup(array_unique))
    # range_print(array_dup)
