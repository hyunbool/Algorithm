# 2016년(https://programmers.co.kr/learn/courses/30/lessons/12901)
def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['WED','THU','FRI','SAT','SUN','MON','TUE']
    
    m = 1
    for i in range(a-1):
        m += month[i]

    return day[(m+b) % 7]