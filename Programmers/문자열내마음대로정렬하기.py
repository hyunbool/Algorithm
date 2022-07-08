# 문자열 내 마음대로 정렬하기(https://school.programmers.co.kr/learn/courses/30/lessons/12915)

def solution(strings, n):
    sorted_strings = sorted([s[n]+s for s in strings])
    answer = [s[1:] for s in sorted_strings]
    return answer

"""
# lanbda의 key를 사용하여 정렬
# sorted(strings, key=lambda x: x[n])
"""