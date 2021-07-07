"""
2번. 메뉴 리뉴얼
"""
from itertools import combinations

def solution(orders, course):
    result = []
    
    for num in course:
        combination = list()
        for menu in orders:
            food = sorted(list(menu))
            foods = list(map(lambda x: ''.join(x), combinations(list(food), num)))
            print(foods)      
            if foods: # tmp가 빈 리스트가 아닐 때
                combination += foods

        count = dict.fromkeys(list(set(combination)), 0)
        for comb in combination:
            count[comb] += 1

        
        if len(count) <= 1:
            continue
            
        dict_max = max(count.values())
        
        if dict_max <= 1:
            continue
        for key, value in count.items():
            if value == dict_max:
                result.append(key)
    
    return sorted(result)