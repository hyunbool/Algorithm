# 시저 암호(https://school.programmers.co.kr/learn/courses/30/lessons/12926)

def solution(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy'
    answer = ''
    
    for c in s:
        if c == " ":
            answer += c
            continue
        
        if c.isupper(): # 대문자이면
            c = c.lower()
            answer += alphabet[alphabet.index(c) + n].upper()
        else:
            answer += alphabet[alphabet.index(c) + n]
    return answer