# 두 정수 사이의 합(https://school.programmers.co.kr/learn/courses/30/lessons/12912)
def solution(a, b):
    int_list = sorted([a, b])
    int_list = [i for i in range(int_list[0], int_list[1]+1)]
    return sum(int_list)

"""
# abs와 수열 합 공식을 사용하자
# (abs(a-b)+1)*(a+b)//2
"""