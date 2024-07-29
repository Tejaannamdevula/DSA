class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Que:

    def __init__(self, size) -> None:
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, data):  # O(1)
        node = Node(data)
        if self.tail is None:
            self.tail = self.head = node
        else:

            self.tail.next = node
            self.tail = node

    def dequeue(self):  # O(1)
        if self.isEmpty():
            raise IndexError("Queue is empty")

        front = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return front

    def peek(self):  # O(1)
        if self.isEmpty():
            raise IndexError("Queue is empty")

        return self.head.data

    def __str__(self) -> str:
        if self.isEmpty():
            return "Queue is empty"
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return " ".join(map(str, elements))


# q = Que(3)
# q.enqueue(1)
# # q.enqueue(2)
# # q.enqueue(3)
# print(q)
# print("removed element is", q.dequeue())
# print(q)
