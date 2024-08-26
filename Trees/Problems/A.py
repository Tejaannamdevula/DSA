# cook your dish here
import sys

import os
import sys
from io import BytesIO, IOBase

# endregion
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")
# sys.stderr = open("error.txt", "w")


from collections import defaultdict
import math
import time
from queue import PriorityQueue


def main():
    """
    node should be 1 and all of its children should be 1 then we delete

    if node is initially removable it will be removable

            O 1
            |                               O 1      
            O  1                =>      /   |   \    =>     /  |  \    
        /   |   \                       O 1 O 1  O 1        O   O  O  attached to some 
       O 1   O 1    O 1                                               other node if now it              
                                                                  is removable we will be removing it before only
                                                                  so deletions wont change anything (Observation)
                                              

    """

    n = int(input())
    children = defaultdict(list)

    c = [0] * (10**5 + 1)
    for i in range(n):
        parent, val = map(int, input().split())
        c[i + 1] = val
        if parent != -1:
            children[parent].append((i + 1, val))

    ans = []

    for i in range(1, len(c)):
        if c[i] == 1:
            possible = 1
            for x in children[i]:
                if x[1] == 0:
                    possible = 0
                    break

            if possible:
                ans.append(i)

    if ans:
        print(*ans)
    else:
        print(-1)


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


if __name__ == "__main__":
    main()
