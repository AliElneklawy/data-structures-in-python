class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):

        if self.head is None:
            self.head = Node(data, None)
            return
        
        trav = self.head
        while trav.next:
            trav = trav.next

        trav.next = Node(data, None)

    def insert_beg(self, data):
        temp = self.head
        self.head = Node(data, temp)

    def insert_at(self, data, idx):
        if idx < 0 or idx > self.length - 1:
            raise Exception("Invalid index")
        
        if idx == 0:
            self.insert_beg(data)
            return
        elif idx == self.length - 1:
            self.insert_end(data)
            return
        
        cnt, trav = 0, self.head
        while cnt < idx-1:
            trav = trav.next
            cnt += 1

        temp = trav.next
        node = Node(data, temp)
        trav.next = node

    def remove_end(self):
        trav = self.head
        
        while trav.next.next:
            trav = trav.next

        trav.next = None

    def remove_beg(self):
        self.head = self.head.next

    def remove_at(self, idx):
        if idx < 0 or idx > self.length - 1:
            raise Exception("invalid index")
        
        if idx == 0:
            self.remove_beg()
            return
        elif idx == self.length - 1:
            self.remove_end()
            return
        
        cnt, trav = 0, self.head
        while cnt < idx-1:
            trav = trav.next
            cnt += 1

        temp = trav.next
        trav.next = temp.next
        temp.next = None


    def print(self):
        iter = self.head
        while iter:
            print(iter.data, end=' ---> ' if iter.next else '\n')
            iter = iter.next

    @property
    def length(self):
        cnt, iter = 0, self.head

        while iter:
            cnt += 1
            iter = iter.next

        return cnt
        


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_end(1)
    ll.insert_end(2)
    ll.insert_end(3)
    ll.insert_end(4)
    ll.insert_beg(0)
    ll.insert_beg(-1)
    ll.insert_beg(-2)
    ll.insert_end(5)
    ll.insert_beg(-3)
    ll.insert_at(-4, 0)
    ll.insert_at(6, 2)
    ll.print()
    ll.remove_at(5)
    ll.print()
    