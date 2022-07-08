# 같은숫자는싫어(https://school.programmers.co.kr/learn/courses/30/lessons/12906)
def solution(arr):
    tmp = arr[0]
    answer = [arr[0]]
    for a in arr:
        if tmp != a:
            answer.append(a)
            tmp = a
    return answer