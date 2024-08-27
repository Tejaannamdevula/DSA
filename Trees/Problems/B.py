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
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


def main():
    """
    we go to only childrens ...choose any children and  go to depth till leaf

    we solve for each children same problem i.e expected length of sub treee


    Expected value = sigma pi * i
        pi =  probability of  getting into the sub tree ( 1/children)
        ai = value of sub tree


        Now Task is to do Recursively  ==> TREE DP

        dp [i] ----> expected value of length in subtree i
        dp[i ] = 1 + avg(dp[children of i])

        can do with dfs  but no dp since no overlapping sub problems here
        each vertex comes form exactly one parent no need to store and we can return it

    """
    N = int(input())
    adj_list = defaultdict(list)
    for i in range(N - 1):
        u, v = map(int, input().split())
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(
            u - 1
        )  # cant add single because form the input we cant figure parent

    dp = [0] * N

    @bootstrap
    def dfs(curr, parent):
        value = 0.0

        nchilds = 0

        for vertex in adj_list[curr]:
            if vertex != parent:
                nchilds += 1
                value += yield dfs(vertex, curr)

        if nchilds == 0:
            yield 0
        else:
            yield 1 + value / nchilds

    print(dfs(0, -1))


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
