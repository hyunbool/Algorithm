"""
1) 팀장이 참석하는 경우(서브트리의 루트가 선택된 경우): 팀원 전원이 참석하지 않아도 이미 팀장이 참여했기 때문에 조건 만족
    - 서브트리 각 자식 노드들에 대해 선택하거나
    - 선택하지 않은 경우의 최소 가중치를 모두 구해 작은 값들만을 더해주기
2) 팀장이 참석하지 않는 경우:각 자식 노드의 참석/불참 가중치를 구해, 더 작은 값을 취할때 하나라도 참석 시 가중치가 적어 선택이 된다면 문제가 없음

- 그룹장이 워크숍에 참석하는 경우 -dp[n][1]
- 그룹장이 워크숍에 참석하지 않는 경우 - dp[n][0]
"""

graph = [list() for _ in range(300000)]
visited = [0 for _ in range(300000)]
dp = [[0]* 2 for _ in range(300000)]

def dfs(parent):
    if not graph[parent]:
        # 리프인 경우
        dp[parent][0], dp[parent][1] = s[parent], 0

        return None

    value = 10000000

    dp[parent][0] = s[parent]

    for x in graph[parent]:
        dfs(x)
        dp[parent][0] += min(dp[x])
        value = min(value, dp[x][0] - dp[x][1])

    if value < 0:
        value = 0

    dp[parent][1] = dp[parent][0] + value - s[parent]

def solution(sales, links):
    global s
    s = [0] + sales # 1번부터 시작하기 위해 조작
    
    # graph 만들기
    for link in links:
        graph[link[0]].append(link[1])
    
    # 루트부터 시작하기
    dfs(1)

    return min(dp[1])
