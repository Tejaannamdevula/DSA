import time

"""
        it is a piece wise functi0n 

                    
                    0  if n ==0 
        fib(n ) =   1  if n ==1
                    fib(n-1) + fib(n-2) 
"""
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(50))
memo  ={}
def fib_top_down(n):
    if n<2:
        return n
    if n not  in memo:
        memo[n] = fib_top_down(n-1)+fib_top_down(n-2)
    return memo[n]
start = time.time()
print(fib_top_down(5))
print("time for topdown",time.time()- start)


"""
            pull dp answer of current is caluculated or pulled   form previous
"""
def fib_bottom_up(n):
    dp = [0,1]
    for i in range(2,n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
    

start = time.time()
print(fib_bottom_up(5))
print("time for bottomup",time.time()- start)


"""
            push  dp based on current future  states are updated
"""

def fib_push(n):
    dp = [0]*(n+1)
    dp [1] = 1
    for i in range(1,n):
        dp[i+1] += dp[i]
        if i+2<=n:
            dp[i+2] += dp[i]
    
    return dp[n]


start = time.time()
print("fib push",fib_push(5))
print("time for push",time.time()- start)