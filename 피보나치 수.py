import sys
sys.setrecursionlimit(10**6)
d = d = {0: 0, 1: 1, 2: 1}

def fibo(n):
    if n in d:
        return d[n]
    else:
        a = fibo(n-1) + fibo(n-2)
        d[n] = a
        return a

def solution(n):
    return fibo(n) % 1234567