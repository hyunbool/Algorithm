# 두개 뽑아서 더하기(https://programmers.co.kr/learn/courses/30/lessons/68644)
from itertools import combinations

def solution(numbers):
    comb_sum = list(set([c[0] + c[1] for c in list(set((combinations(numbers, 2))))]))

    return sorted(comb_sum)