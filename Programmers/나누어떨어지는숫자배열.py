# 나누어 떨어지는 숫자 배열(https://school.programmers.co.kr/learn/courses/30/lessons/12910)
def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
            
    if len(answer) == 0:
        return [-1]
    
    return sorted(answer)