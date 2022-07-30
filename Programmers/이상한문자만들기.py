# 이상한 문자 만들기(https://school.programmers.co.kr/learn/courses/30/lessons/12930)

def solution(s):
    answer = ''
    word = s.split(" ")
    for w in word:
        for i, c in enumerate(w):
            if i % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        answer += " "
    return answer[:-1]