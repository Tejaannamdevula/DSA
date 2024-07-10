class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("stack is empty")
        val = self.stack.pop()
        self.size -= 1
        return val

    def peek(self):
        if self.size == 0:
            raise IndexError("stack is empty")
        return self.stack[-1]

    def getSize(self):
        return self.size

    def __str__(self) -> str:
        # values = [str(i) for i in self.stack]
        # return " ".join(values)

        return " ".join(map(str, self.stack))


s = Stack()

s.push(1)
s.push(2)
s.push(3)
print(s)
s.pop()
print(s)
s.peek()
print(s)
