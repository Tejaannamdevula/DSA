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
            valid minutes          valid minutes at end
               _______             _____
                1   3   5   2   5   4
                1   1   0   1   0   0
                        _________
                            k(min)


            ans =  valid minute thereoms +  k range theorems + valid minutes at end theorems
                =    (1+3)  + (5+2+5) + (0)
                =    16

            need to maximize this answer

            valid prefix sum sum of all elemts till i whose awake val = 1
            similarly for valid suffix sum

                    shortcut  =  awake[i]* theorems[i]  if 0 then val = 0  

            prefix sums for caluculating sum in ragee i,j =  prefix[j] - prefix[i-1]



    """

    n,k = map(int,input().split())
    theorems  = list(map(int,input().split()))
    awake = list(map(int,input().split()))

    valid_prefix_sum = [0]*n
    
    valid_prefix_sum[0] = theorems[0]*awake[0]

    for i in range(1,n):
        valid_prefix_sum[i] = valid_prefix_sum[i-1] + theorems[i]*awake[i]
     
    valid_suffix_sum = [0]*n

    valid_suffix_sum[n-1] = theorems[n-1]*awake[n-1]

    for i in range(n-2,-1,-1):
        valid_suffix_sum[i]  =  theorems[i]*awake[i]  + valid_suffix_sum[i+1]

    prefix_sum  = [0]*n
    s  = 0
    for i in range(n) :
        s += theorems[i]
        prefix_sum[i]   = s

    ans = 0

    # print("valid prefix_sum",valid_prefix_sum)
    # print("valid suffix_sum",valid_suffix_sum)
    # print(" prefix_sum",prefix_sum)
    count = 0

    for i in range(0,n-k+1,1):
        curr_sum = 0
        if i>0 :
            curr_sum += valid_prefix_sum[i-1]
        if i+k<n:
            curr_sum+= valid_suffix_sum[i+k]

        range_sum = prefix_sum[i+k-1] - prefix_sum[i-1]
        curr_sum += range_sum
        count+=1
        ans = max(curr_sum,ans)

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