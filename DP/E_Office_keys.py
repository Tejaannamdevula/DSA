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

            position         A   B 
                                        

            key                 C    D   best path is A to C and  and B to D ( not crossing paths is better ) give A,B and C,D are sorted

            assignments of keys are in increasing order 

                        1  2 3 4 5 (keys)
                when assigning 3rd person key we already assigned previous ones 

            dp (position,lastperson)   min cost till lastperson 

            dp[i][j]  minimum time needed for first i people using first j keys

            ans = min i (dp[i][n])  final position dont matter we need to use all n people

                                        take            dp(pos+1,lastperson+1)
            dp(pos,lastperson)  
                                        dont take       dp(pos+1,lastperson)
                
            base case dp[0][0]  = 0  and rest inf
        
    """

    n,k,p  = map(int,input().split())
    positions = list(map(int,input().split()))
    keys = list(map(int,input().split()))

    positions.sort()
    keys.sort()

    # dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
    # dp[0][0]  = 0
    # for i in range(k):
    #     for j in range(n+1):
    #         #dont take 
    #         dp[i+1][j]  = min(dp[i+1][j], dp[i][j])

    #         # do take
    #         if j< n:

    #             dp[i+1][j+1]  = min(dp[i+1][j+1] ,max(dp[i][j], abs(positions[j] - keys[i]) +abs(keys[i] - p)))

    # print(dp[k][n])

    dp =  [[float('inf')]*(k+1) for _ in range(n+1)]
    dp[0][0]  = 0     #selcting 0 persons usinf k keys

    # print(dp)

    for i in range(n):
        for j in range(k+1):
            
            dp[i+1][j]  = min(dp[i+1][j],dp[i][j])
            if j <k  :
                # print("aaa",dp[i][j])
                # print("bbbb",positions[i])
                # print("ccc",keys[j-1])
                # # print("ddd",dp[i+1][j+1])
                # print("aaabbbbbbbbb",abs(positions[i]- keys[j]) +abs(keys[j] -p) )

                dp[i+1][j+1]  = min(dp[i+1][j+1] , max(dp[i][j],abs(positions[i]- keys[j-1]) +abs(keys[j-1] -p) ))

            print(f"i{i} ")
            print(dp)
            

    print(min(dp[n][1:]))
    





    



            

             
            




        


           
        
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