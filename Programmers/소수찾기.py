# 소수 찾기(https://school.programmers.co.kr/learn/courses/30/lessons/12921)

import math

# 에라스토테네스의 채 사용하기!
def solution(n):
    arr = [True for _ in range(n+1)]
    arr[0] = False
    arr[1] = False
    
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i] == True:
            j = 2
            
            while j*i <= n:
                arr[j * i] = False
                j += 1
            
    return arr.count(True)