# 비밀지도(https://programmers.co.kr/learn/courses/30/lessons/17681)
def solution(n, arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        x = format(arr1[i], 'b')
        y = format(arr2[i], 'b')
        if len(x) < n:
            x = '0' * (n - len(x)) + x
        if len(y) < n:
            y = '0' * (n - len(y)) + y
        
        tmp = ''
        
        for j in range(n):
            if x[j] == '1' or y[j] == '1': 
                tmp += '#'
            else:
                tmp += ' '

        answer.append(tmp)

    return answer