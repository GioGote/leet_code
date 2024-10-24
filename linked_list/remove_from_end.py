class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# 19. Remove Nth node for end of list
def remove_nth_from_end(head, int):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while int > 0 and right:
        right = right.next
        int -= 1

    while right:
        left = left.next
        right = right.next

    # delete node
    left.next = left.next.next
    return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values)))

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])
    
    # Print the original linked list
    print("Original linked list:")
    print_linked_list(head)

    # Remove the 2nd node from the end
    n = 2
    head = remove_nth_from_end(head, n)

    # Print the modified linked list
    print(f"Linked list after removing the {n}th node from the end:")
    print_linked_list(head)