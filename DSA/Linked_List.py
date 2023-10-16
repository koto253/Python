Class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next 

Class Linked_list:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_linked_list = Linked_list(4)

print(new_linked_list.head)
