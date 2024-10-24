# ARRAYS BUT BETTER
# Nodes: 
# 1. Value - anything strings, integers, objects
# 2. The Next Node

# __init__ is an instance method that initializes a newly created object

class linkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

# "3" -> "7" -> "10"

node1 = linkedListNode("3")
node2 = linkedListNode("7")
node3 = linkedListNode("10")
node4 = linkedListNode("77")

node1.next_node = node2
node2.next_node = node3
node3.next_node = node4

# node1 -> node2 -> node3

# collect values in a list
values = []
current_node = node1

while current_node is not None:
    values.append(current_node.value)
    current_node = current_node.next_node

# print in one line
print(" -> ".join(values) + " -> None")

# ******************************************************************************************************************************************
# NOW THE CHAD METHOD

'''
# Still needed
class linkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
'''

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        
        current_node = self.head
        while True:
            if current_node.next_node is None:
                current_node.next_node = node
                break
            
            current_node = current_node.next_node

    def printLinkedList(self):
        current_node = self.head
        values = []
        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.next_node

        print(" -> ".join(values) + " -> None")

print("\n")

ll = linkedList()
ll.insert("3")
ll.printLinkedList()
ll.insert("44")
ll.printLinkedList()
ll.insert("55")
ll.printLinkedList()