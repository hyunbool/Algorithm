# 뉴스 클러스터링(https://programmers.co.kr/learn/courses/30/lessons/17677)


import re

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_list = []
    for i in range(len(str1)-1):
        s1 = re.sub(r'[^가-힝A-z]+', '', str1[i:i+2]).replace('_', '')
        if len(s1) == 2:
            str1_list.append(s1)
                
    str2_list = []
    for i in range(len(str2)-1):
        s2 = re.sub(r'[^가-힝A-z]+', '', str2[i:i+2]).replace('_', '')
        if len(s2) == 2:
            str2_list.append(s2)
    
    # 합집합 구하기
    sumset = str1_list.copy()
    tmp = str1_list.copy()

    result = list()
    for s2 in str2_list:
        if s2 in tmp:
            tmp.remove(s2)
            result.append(s2)
        else:
            sumset.append(s2)

    if len(sumset) == 0:
        return 65536
    else:
        sim = (len(result) / len(sumset)) * 65536

        return int(sim)