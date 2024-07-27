class CircularQueue:
    def __init__(self, size) -> None:
        self.q = [0] * size
        self.size = size
        self.front = -1
        self.rear = -1
        pass

    def isEmpty(self):
        return self.rear == self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):  # O(1)
        if self.isFull():
            raise IndexError("Queue is full")

        if self.front == -1:
            self.front += 1  # adding first element
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = data

    def dequeue(self):  # O(1)
        if self.isEmpty():
            raise IndexError("Queue is empty")

        element = self.q[self.front]
        if self.rear == self.front == 0:  # single element
            self.rear = self.front = -1
        self.front = (self.front + 1) % self.size

        return element

    def peek(self):  # O(1)
        if self.isEmpty():
            raise IndexError("Queue is empty")
        return self.q[self.front]

    def __str__(self) -> str:
        if self.isEmpty():
            return "Queue is Empty"

        if self.rear >= self.front:  # rear is ahead of front
            return " ".join(map(str, self.q[self.front : self.rear + 1]))

        first_part = " ".join(map(str, self.q[self.front : self.size]))
        second_part = " ".join(map(str, self.q[: self.rear + 1]))
        return first_part + " " + second_part


# q = CircularQueue(3)

# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q)
# print(q.dequeue())
# print(q)

# q.enqueue(5)
# print(q.q)
# print(q)
