# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it

# there is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer, internally, pos is used to denote the index
# of the node that tail's next pointer is connected to. Note that pos is not passed as a param.

# return True if there is a cycle in the linked list. otherwise, retunr False

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    dummy = ListNode()
    dummy.next = head
    slow = fast = dummy

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow is fast:
            return True
        
    return False

    '''
    if head is None:
        return False

    slow = head  # Tortoise
    fast = head  # Hare

    while fast and fast.next:
        slow = slow.next        # Move slow pointer by 1
        fast = fast.next.next   # Move fast pointer by 2

        if slow == fast:  # Cycle detected
            return True

    return False  # No cycle found
    '''

# Example usage:
# Creating a linked list with a cycle for testing
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creating a cycle here

print(hasCycle(node1))  # Should print True