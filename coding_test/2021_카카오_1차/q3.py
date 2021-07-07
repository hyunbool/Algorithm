from itertools import combinations

"""
선형 검색 ver
"""

def linear_solution(info, query):
    info = list(map(lambda x: x.split(" "), info))
    query = list(map(lambda x: x.replace(' and', '').split(" "), query))
    result = list()

    for q in query:
        count = 0
        q =  [item for item in q if item != '-']
        for person in info:
            if (int(person[-1]) >= int(q[-1])) and (set(q[:-1]).issubset(set(person))):
                count += 1
        result.append(count)

    return result

"""
최적화 ver
"""

def optimal_solution(info, query):
    info = list(map(lambda x: x.split(" "), info))
    query = list(map(lambda x: x.replace(' and', '').split(" "), query))
    result = list()
    all_info = dict()
    all_info["-----"] = list() # 점수만 고려하는 경우 위해 초기화
    answer = []

    for person in info:
        score = person[-1]
        all_info["-----"].append(score)
        for num in range(1, len(person)+1):
            tmp = list(map(lambda x: sorted(list(x)), combinations(person[:-1], num)))
            for t in tmp:
                t = "".join(t)
                if not all_info.get(t):
                    all_info[t] = [int(score)]
                else:
                    all_info[t].append(int(score))

    # 이진 탐색 위해 정렬
    for key in all_info.keys():
        all_info[key].sort()


    for q in query:
        count = 0
        q = sorted([item for item in q if item != '-'])
        score = q[0]
        cond = "".join(q[1:])

        # 점수만 고려(탐색하지 않아도 됨)
        if cond in all_info.keys():
            print(all_info[cond])
            answer.append(len(all_info[cond]) - bisect_left(all_info[cond], int(score), lo=0, hi=len(all_info[cond])))

        elif len(cond) < 1:
            tmp = all_info['-----']
            answer.append(len([ x for x in tmp if int(x) >= int(score)]))
        
        else:
            answer.append(0)

    return answer
