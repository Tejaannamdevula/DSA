class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def insert_first(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_last(self, val):
        if not self.head:
            self.insert_first(val)
        else:
            node = Node(val)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def insert(self, val, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insert_first(val)
        elif index == self.size - 1:
            self.insert_last(val)
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            node = Node(val)
            node.next = temp.next
            temp.next.prev = node
            temp.next = node
            node.prev = temp
            self.size += 1

    def delete_first(self):
        if not self.head:
            raise IndexError("linked list is empty")
        else:
            val = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size = 0
            return val

    def delete_last(self):
        if self.size <= 1:
            if not self.head:
                raise IndexError("linked list is empty")
            else:
                val = self.head.data
                self.head = self.tail = None
                self.size = 0
            return val
        else:
            val = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None

            self.size -= 1

            return val

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.delete_first()
        elif index == self.size - 1:
            return self.delete_last()
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            val = temp.next.data
            temp.next.next.prev = temp
            temp.next = temp.next.next
            self.size -= 1
            return val

    def find(self, val):
        temp = self.head
        if not temp:
            return False
        while temp:
            if temp.data == val:
                return True
            temp = temp.next

        return False

    def __str__(self) -> str:
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        return " <=> ".join(values)


dll = DLL()

dll.insert_last(1)
# print(dll.delete_first())
dll.insert_first(2)

# dll.insert_first(3)
# print(dll.delete_last())

# dll.insert_last(4)
# dll.insert(5, 3)
# print(dll)
# dll.insert(6, 1)
dll.delete(0)
print(dll)


# print(dll.find(1))
# print("size after inserting 5", dll.size)
# print(dll)
