# 신고 결과 받기(https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3)

def solution(id_list, report, k):
    report_dict = {} # 키: 유저, 값: 유저가 신고한 id
    id_dict = {} # 신고당한 횟수
    answer = [0 for _ in range(len(id_list))]
    
    for id in id_list:
        report_dict[id] = []
        id_dict[id] = 0
    
    reported_id = [r.split(" ") for r in list(set(report))]

    for r in reported_id:
        report_dict[r[0]].append(r[1])
        id_dict[r[1]] += 1

    over_k = list(dict(filter(lambda elem:elem[1]>=k, id_dict.items())))

    for i, id in enumerate(report_dict):
        mail = set(report_dict[id]) & set(over_k)
        answer[i] = len(mail)
        
    
    return answer