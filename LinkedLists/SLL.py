class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SLL:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def insert_first(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insert_last(self, val):
        if not self.head:
            self.insert_first(val)
            return

        node = Node(val)
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = node
        self.size += 1

    def insert(self, val, index):
        if index == 0:
            self.insert_first(val)
            return
        if index == self.size:
            self.insert_last(val)
            return

        node = Node(val)

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

        node.next = temp.next
        temp.next = node

        self.size += 1

    def delete_first(self):
        if not self.head:
            raise IndexError("Linked list is empty")
        else:
            val = self.head.data
            self.head = self.head.next
            self.size -= 1
            return val

    def delete_last(self):
        if self.size == 0:
            raise IndexError("Linked list is empty")
        if self.size <= 1:
            return self.delete_first()

        second_last_node = self.head
        while second_last_node.next.next is not None:
            second_last_node = second_last_node.next

        val = second_last_node.next.data
        second_last_node.next = None
        self.size -= 1
        return val

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        temp = self.head
        if index == 0:
            return self.delete_first()

        if index == self.size - 1:
            return self.delete_last()

        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        val = temp.next.data
        temp.next = temp.next.next
        self.size -= 1
        return val

    def find(self, val):
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False

    def __str__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return "->".join(values)


sll = SLL()
sll.insert_first(1)
sll.insert_last(2)
sll.insert(3, 2)
sll.insert_first(4)
sll.insert_first(5)
sll.insert_first(6)
print(sll)
print(sll.delete_first())
print(sll)
print(sll.delete_last())
print(sll)
print(sll.delete(3))
print(sll)
print(sll.delete(0))
print(sll)
