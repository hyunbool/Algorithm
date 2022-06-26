# 다트 게임(https://programmers.co.kr/learn/courses/30/lessons/17682)
def solution(dartResult):
    region = [0, 'S', 'D', 'T']
    star = '*'
    minus = '#'
    
    results = [c for c in dartResult]
    
    score_cur = 0
    cur = [] 
    for i, r in enumerate(results):
        if r == star:
            cur.append('*')
        elif r == minus:
            cur[-1] = (-1) * cur[-1]
        elif r in region:
            score = score_cur ** int(region.index(r))
            score_cur = 0
            cur.append(score)
        else:
            score_cur = int(r)
            if r == '0' and results[i-1] == '1':
                score_cur = 10

        

    tmp = []
    for i in range(0, len(cur)):
        if cur[i] == star:
            tmp[-1] *= 2
            if len(tmp) == 1:
                continue
            else:
                tmp[-2] *= 2

        else:
            tmp.append(cur[i])

    return sum(tmp)