# 최대공약수와 최소공배수(https://school.programmers.co.kr/learn/courses/30/lessons/12940#)
"""
문제 설명:
    - 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
"""

# 유클리드 호제법: a, b의 최대공약수와 b, r(a%b의 나머지) 의 최대공약수가 같다는 성질


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
            
def solution(n, m):
    answer = []
    n, m = sorted([n, m])

    gcd_num = gcd(n, m)

    return [gcd_num, n*m/gcd_num]