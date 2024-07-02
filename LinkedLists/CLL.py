class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None


class CircularSLL:
    def __init__(self) -> None:
        self.tail = None
        self.size = 0

    def is_empty(self):
        # Returns True if the list is empty, otherwise False
        return self.size == 0

    def get_size(self):
        return self.size

    def insert_first(self, val):
        # Inserts an element at the beginning of the list
        node = Node(val)
        if self.tail is None:
            self.tail = node
            self.tail.next = self.tail
        else:
            node.next = self.tail.next
            self.tail.next = node
        self.size += 1

    def insert_last(self, val):
        # Inserts an element at the end of the list
        if self.size == 0:
            self.insert_first(val)
            return
        node = Node(val)
        node.next = self.tail.next
        self.tail.next = node
        self.tail = node
        self.size += 1
        pass

    def insert(self, val, index):
        # Inserts an element at the specified index
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insert_first(val)
        elif index == self.size:
            self.insert_last(val)
        else:
            head = self.tail.next
            for i in range(index - 1):
                head = head.next
            node = Node(val)
            node.next = head.next
            head.next = node
            self.size += 1
        pass

    def delete_first(self):
        # Deletes the first element of the list
        if self.size == 0:
            raise IndexError("linked list is empty")
        elif self.size == 1:
            val = self.tail.data
            self.tail = None
        else:
            val = self.tail.next.data
            self.tail.next = self.tail.next.next
        self.size -= 1
        return val

    def delete_last(self):
        # Deletes the last element of the list
        if self.size <= 1:
            return self.delete_first()
        else:
            val = self.tail.data
            head = self.tail.next
            while head.next != self.tail:
                head = head.next
            head.next = self.tail.next
            self.tail = head
            self.size -= 1
            return val

        pass

    def delete(self, index):
        # Deletes the element at the specified index
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            return self.delete_first()
        elif index == self.size - 1:
            return self.delete_last()
        else:
            temp = self.tail.next

            for i in range(index - 1):
                temp = temp.next
            val = temp.next.data
            temp.next = temp.next.next
            self.size -= 1

            return val
        pass

    def find(self, val):
        # Finds the element in the list and returns True if it exists, otherwise False
        head = self.tail.next
        if not head:
            return False
        while True:
            if head.data == val:
                return True
            head = head.next
            if head == self.tail.next:
                break
        return False
        pass

    def __str__(self) -> str:
        # Returns a string representation of the list

        if self.is_empty():
            return "List is empty"

        head = self.tail.next
        values = []
        while True:
            values.append(str(head.data))
            head = head.next
            if head == self.tail.next:
                break
        return "->".join(values)
        pass


# Testing the CircularSLL class
cll = CircularSLL()

cll.insert_first(1)
print(cll)  # Output: 1

cll.insert_last(2)
print(cll)  # Output: 1->2

cll.insert(3, 1)
print(cll)  # Output: 1->3->2

print(cll.find(1))  # Output: True
print(cll.find(2))  # Output: True
print(cll.find(3))  # Output: True
print(cll.find(4))  # Output: False

print(cll.delete_first())  # Output: 1
print(cll)  # Output: 3->2

print(cll.delete_last())  # Output: 2
print(cll)  # Output: 3

print(cll.delete(0))  # Output: 3
print(cll)  # Output: List is empty
