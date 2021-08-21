import math
def solution(arr):
    length = len(arr)
    g = arr[0]
    for i in range(length):
        g = g * arr[i] // math.gcd(g, arr[i])
    return g