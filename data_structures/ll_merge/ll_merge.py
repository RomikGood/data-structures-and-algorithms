from .node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._length = 0

    def __len__(self):
        return self._length

    def includes(self, value) -> bool:
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def insert(self, data):
        self.head = Node(data)
        # self._length += 1

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            self._length += 1
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print('revious node is not in the list')
        
        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node

    def merge_sorted(self, llist):
        '''function takes linked list as a parameter and merges
        it with orrriginal linked list
        '''
        p = self.head
        q = llist.head
        temp = None

        if not p:  # if only one list exists return another
            return q
        if not q:  # if only one list exists return another
            return p
        if p and q:
            if p.data <= q.data:
                temp = p
                p = temp.next
            else:
                temp = q
                q = temp.next
            new_head = temp
        while p and q:
            if p.data <= q.data:
                temp.next = p
                temp = p
                p = temp.next
            else:
                temp.next = q
                temp = q
                q = temp.next
        if not p:
            temp.next = q
        if not q:
            temp.next = p
        return new_head


# llist1 = LinkedList()
# llist2 = LinkedList()

# llist1.append(1)
# llist1.append(5)
# llist1.append(7)
# llist1.append(9)
# llist1.append(10)

# llist2.append(2)
# llist2.append(3)
# llist2.append(4)
# llist2.append(6)
# llist2.append(11)


# if __name__ == '__main__':
#     llist1.merge_sorted(llist2)
#     llist1.print_list()
