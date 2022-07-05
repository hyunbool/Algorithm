import math

def find_div(n):
    arr = []
    for i in range(2, n+1):
        if n % i == 0:
            arr.append(i)
    return arr


def solution(n): 
    return min(find_div(n-1))