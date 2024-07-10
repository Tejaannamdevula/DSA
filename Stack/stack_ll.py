import sys
import os

# Add the parent directory (DSA) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from LinkedLists.SLL import SLL

# sll = SLL()
# print("SLL initialized:", sll)


class Stack_LL:
    def __init__(self) -> None:
        self.stack = SLL()

    def push(self, data):
        self.stack.insert_first(data)

    def pop(self):
        if self.getSize() == 0:
            raise IndexError("Stack is empty")
        return self.stack.delete_first()

    def getSize(self):
        return self.stack.size

    def peek(self):
        if self.getSize() == 0:
            raise IndexError("Stack is empty")

        return self.stack.head.data

    def __str__(self) -> str:
        if self.getSize() == 0:
            return "Stack is empty"

        current = self.stack.head
        stack_str = ""
        while current:
            stack_str = str(current.data) + " -> " + stack_str
            current = current.next
        return stack_str.rstrip(" -> ")


if __name__ == "__main__":
    s = Stack_LL()

    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    s.pop()
    print(s)
    s.peek()
    print(s)
