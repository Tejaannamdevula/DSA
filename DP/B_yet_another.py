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
        abacaba             a,b

        1 => can type 
        0 => cant type using a,b

        abacaba => 1110111   no of substring has all 1

        f(i) => number of substrings ending at i 
        
        if s[i] == 0  ==> f(i) == 0
        

        f(i) = 1+  f(i-1)    adding the current char to all previous substring  1 for current char 


        ans = sum(f[i])

        base case:
            f(0)  = 1 ending at 0 th index 

                    or
                another approach

            f(0) = 0 
            f = [0]*(n+1)
            and use 1 based idnexing    
            f(i)  substring ending at ith letter

     
    """
    
    n,k = map(int,input().split())
    s = input()
    working_keys=  [False]*26
    for i in (input().split()):
        working_keys[ord(i) - ord('a')] = True
    arr = [0]*n 
    for i,j in enumerate(s):
        if working_keys[ord(j)-ord('a')]:
            arr[i] = 1
        else:
            arr[i] = 0

    f = [0]*n
    if arr[0] == 1:
        f[0]  = 1

    for i in range(1,n):
        if arr[i]!= 1:
            f[i]  = 0
        else:
            f[i] =  f[i-1] + 1

    print (sum(f))

             
            




        


           
        
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