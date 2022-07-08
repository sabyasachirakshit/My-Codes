class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def swaplist(self):
        temp = self.head
        if temp is None:
            return
        while(temp is not None and temp.next is not None):
            if(temp.data == temp.next.data):
                temp = temp.next.next
            else:
                temp.data, temp.next.data = temp.next.data, temp.data
                temp = temp.next.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist = linked_list()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print('Linked List before swap:')
llist.printlist()
print('Linked List after Swap:')
llist.swaplist()
llist.printlist()
