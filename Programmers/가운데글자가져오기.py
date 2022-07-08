# 가운데 글자 가져오기(https://school.programmers.co.kr/learn/courses/30/lessons/12903)
def solution(s):
    if len(s) % 2 == 0:
        mid = int(len(s) / 2)
        return s[mid-1:mid+1]
    else:
        mid = int(len(s)/2)
        return s[mid]