# 문자열 내 p와 y의 개수(https://school.programmers.co.kr/learn/courses/30/lessons/12916)

def solution(s):
    s = s.lower()
    if s.count('y') == s.count('p'):
        return True
    else:
        return False