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
from collections import deque


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
    2  5 4 belong to a group
    means   2 ---- 4
            5 ---- 4
            2 ----- 5

    if people are more in a group then its difficult
    to take all of them and create edges
    to make them reachable its easy to for
        2 ---- 5 ----- 4 or
        connect 2 to 5 and  2 to 4  so edges are reduced


        2 --- 5 ---- 4   for 2 its a connected component and find its size

        doing by bfs now
    """

    N, groups = map(int, input().split())
    adj_list = defaultdict(list)
    for _ in range(groups):
        arr = list(map(int, input().split()))
        k = arr[0]
        for i in range(1, k + 1):
            if i + 1 < k + 1:
                adj_list[arr[i] - 1].append(arr[i + 1] - 1)
                adj_list[arr[i + 1] - 1].append(arr[i] - 1)

    ans = [0] * N
    # for i in range(N):
    #     # if not visited[i]:
    #     visited = [0] * N
    #     component = []
    #     queue = deque()
    #     queue.appendleft(i)
    #     while len(queue) > 0:
    #         curr = queue.pop()
    #         if visited[curr]:
    #             continue
    #         visited[curr] = 1
    #         component.append(curr)
    #         for vertex in adj_list[curr]:
    #             if not visited[vertex]:
    #                 queue.appendleft(vertex)

    #     ans[i] = len(component)

    """
    reduced redundancy
    """
    visited = [0] * N
    for i in range(N):
        if not visited[i]:
            component = []
            queue = deque([i])
            while queue:
                curr = queue.pop()
                if visited[curr]:
                    continue
                visited[curr] = 1
                component.append(curr)
                for vertex in adj_list[curr]:
                    if not visited[vertex]:
                        queue.appendleft(vertex)

            # Set the size of the component for all nodes in the component
            component_size = len(component)
            for node in component:
                ans[node] = component_size
    print(*ans)


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
