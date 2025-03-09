class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None


class DoublyList:
    def __init__(self):
        self.head=None
        self.tail=None 

    def print_forward(self):
        cur = self.head
        while cur:
            print(cur.data, end=" - " if cur.next else "\n")
            cur=cur.next

    def print_backward(self):
        cur=self.tail
        while cur:
            print(cur.data, end=" - " if cur.prev else "\n")
            cur = cur.prev

    def append(self, data):
        new = Node(data)
        if self.head is None:
            self.head = self.tail = new
            new.prev = None
            new.next = None
        else:
            cur = self.head
            while cur.next:
                cur=cur.next
            cur.next=new
            new.prev=cur
            new.next=None
            self.tail=new

    def prepend(self, data):
        new_ = Node(data)
        if self.head is None:
            self.head = self.tail = new_
            new_.prev=None
            new_.next=None
        else:
            new_.next=self.head
            self.head.prev=new_
            self.head=new_
            new_.prev=None

dll = DoublyList()
dll.append(3)
dll.append(2)
dll.append(1)
dll.prepend(4)
dll.prepend(5)

print("Forward traversal:")
dll.print_forward()

print("Backward traversal:")
dll.print_backward()
