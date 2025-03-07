class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None


class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None 

    def print_list_forward(self):
        cur = self.head
        while cur:
            print(cur.data, end=" <-> " if cur.next else "\n")
            cur=cur.next

    def print_list_backward(self):
        cur=self.tail
        while cur:
            print(cur.data, end=" <-> " if cur.prev else "\n")
            cur = cur.prev

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            cur = self.head
            while cur.next:
                cur=cur.next
            cur.next=new_node
            new_node.prev=cur
            new_node.next=None
            self.tail=new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.prev=None
            new_node.next=None
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            new_node.prev=None


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(3)
    dll.append(2)
    dll.append(1)

    dll.prepend(4)
    dll.prepend(5)

    print("Forward traversal:")
    dll.print_list_forward()

    print("Backward traversal:")
    dll.print_list_backward()