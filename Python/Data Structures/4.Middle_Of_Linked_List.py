class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    '''In this class, Operation of Linked List takes place.'''

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        node = self.head
        while node:
            print(str(node.data)+"->", end=" ")
            node = node.next
        print("NULL")

    def print_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("\nThe middle of the list is:", slow.data)


if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 7):
        llist.push(i)
        llist.print_list()
    llist.print_middle()


class linked_list_node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = linked_list_node(1)
node2 = linked_list_node(2)
node3 = linked_list_node(3)
node1.next = node2
node2.next = node3
node3.next = None

current_node = node1
while current_node.next is not None:
    print(current_node.data, "->", end=" ")
    current_node = current_node.next
print("Null")
