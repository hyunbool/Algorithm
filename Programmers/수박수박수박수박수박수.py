# 수박수박수박수박수박수?(https://school.programmers.co.kr/learn/courses/30/lessons/12922)

def solution(n):
    answer = "수박" * int(n/2)
    if n % 2 == 0:
        return answer
    else:
        return answer + "수"