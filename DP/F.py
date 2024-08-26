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


def main():
    """
    n = 4

    permutation 1 2 3 4

    k
    almost identity permutation  is atleat n-k inidices have same index value in array

    k = 1
    n - k = 3 atleat 3

    1 2 3 4  == > one way


    k = 2
    n-k =  2 atlest 2

    1 2 3 4 alteast 3 and 4 is same case

    1 2 4 3
    1 4 3 2
    1 3 2 4
    4 2 3 1
    3 2 1 4
    2 1 3 4


    atleast n- k in order ==>  atmost k out of order order


    let x in [0,k]

    x  = 0  no elements replacing one way

    x =  1  possibilites  = 0

        1 2 3 4

        1 2 3 _  it can only be 4 so we cant do any thing

    x = 2  pick 2 positions to put out of ordder (n 2)
            1 2 3 4
            1 2 4 3   selecting 2 positions out of n    now number of it is out of order  just replace them it will be out of order so ans is (n c 2)

    x = 3   n = 5

        1   2   3    4  5
        _       _       _    selecting 3 positions (n, c, 3)
        1   2  _5    _3  _4

        total positions  = ( n c 3) *  no of ways of placing out of order is 2
                    Ex- a b c
                       1. b a c
                       2. c a b

    x=  4   similary to x = 2 possibilites (n c 4) selecting 4 and number of ways of not in order is D(4) = 9 ==> 9*(n c 4)


    DEARRANGEMENTS  is a permutation of elements in which no element appears in the same order
    NUMBER OF DEARRANGEMENTS  D(N) = (N-1)( D(N-1) + D(N-2))  D(1) = 0 and D(2) = 1


    """

    n, k = map(int, input().split())

    ans = 1
    for x in range(2, k + 1):
        # x = 1 zero already
        if x == 2:
            ans += comb(n, 2)
        elif x == 3:
            ans += comb(n, 3) * 2
        elif x == 4:
            ans += 9 * comb(n, 4)
        # print(x, ans)

    print(ans)


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
