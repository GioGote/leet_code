class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print('None')

# Reverse linked list function
def reverse_linked_list(head):
    # we set a prev node to none and a curr node to the head of the linked list
    prev, curr = None, head
    # while there is a curr linked list (non-empty)
    while curr:
        # nxt node is curr.next
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Example usage
if __name__ == "__main__":
    
    values = [1, 2, 3, 4, 5]  # Create a linked list from this list
    head = create_linked_list(values)

    print("Original linked list:")
    print_linked_list(head)

    # Reverse the linked list
    reversed_head = reverse_linked_list(head)

    print("Reversed linked list:")
    print_linked_list(reversed_head)

    # Note to Self, watch a video on linked lists as a refresher