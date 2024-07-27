class Que:

    def __init__(self, size) -> None:
        self.q = [0] * size
        self.size = size
        self.rear = -1

    def isEmpty(self):
        return self.rear == -1

    def enqueue(self, data):  # O(1)
        if self.rear == self.size - 1:
            raise IndexError("Queue is full")
        self.rear += 1
        self.q[self.rear] = data

    def dequeue(self):  # O(N)
        if self.isEmpty():
            raise IndexError("Queue is empty")

        front = self.q[0]
        for i in range(self.rear):
            self.q[i] = self.q[i + 1]

        self.rear -= 1
        return front

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")

        return self.q[0]

    def __str__(self) -> str:
        return " ".join(map(str, self.q[: self.rear + 1]))


# q = Que(3)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q)
# print("removed element is", q.dequeue())
# print(q)
