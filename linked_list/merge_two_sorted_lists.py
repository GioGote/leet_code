# Leetcode 21. Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new sorted list.
# The new list hsould be made by splicing together the nodes of the first two lists.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2) -> ListNode:
    # use da dummy
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next