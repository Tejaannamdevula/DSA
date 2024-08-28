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

from math import comb
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

    5 _ _ _ _ 6

    change speed is atmost 2

    at each place we increment/decrement for i  to 2

    maximize the sum


    5 _ _ curr_ _ 6

    think solved for previous
        we need to include position
        store prev val to choose the current
    dp(i,prev)


    dp(i,prev )  contributes to dp(i+1, prev +dp) between dp(i+1,prev -dp)


    t = 100
    s <= 10 so maximum s<=1000   need to focus on constraints

    ans is dp[n-1][end] + end

    t = 4  0 1  2 3
           5 7  8 6
    there fore dp[4-1][end] we need

    """
    start, end = map(int, input().split())

    t, d = map(int, input().split())
    INF = 10**20

    # top down
    cache = {}

    # @bootstrap
    def backtrack(index, prev):
        # print(index, prev)
        if index == t:
            if prev == end:
                return end
            else:
                return -INF

        best = -INF
        if (index, prev) in cache:
            return cache[(index, prev)]
        for k in range(-d, d + 1):

            # if index + 1 < t:
            if prev + k > 0 and prev + k < 1000:
                best = max(best, prev + backtrack(index + 1, prev + k))

        cache[(index, prev)] = best
        return best

    print(backtrack(1, start))
    # dp = [[-INF] * 1000 for _ in range(t)]

    # dp[0][start] = 0
    # for i in range(t - 1):
    #     for j in range(1000):
    #         for k in range(-d, d + 1, 1):
    #             if j + k > 0 and j + k < 1000:
    #                 dp[i + 1][j + k] = max(dp[i + 1][j + k], dp[i][j] + j)

    # print(dp[t - 1][end] + end)


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
