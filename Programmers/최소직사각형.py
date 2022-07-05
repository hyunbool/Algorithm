# 최소직사각형(https://school.programmers.co.kr/learn/courses/30/lessons/86491)

def solution(sizes):
    size = [sorted(s) for s in sizes]
    width = max([s[0] for s in size])
    height = max([s[1] for s in size])
    return width * height