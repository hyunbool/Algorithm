def solution(n, s, a, b, fares):

    # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
    INF = int(1e9) 
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if x == y:
                graph[x][y] = 0

    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for i in fares:
        # A에서 B로 가는 비용은 C라고 설정
        x, y, c = i
        graph[x][y] = c
        graph[y][x] = c

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])


    answer = graph[s][1] + graph[1][a] + graph[1][b]
    for k in range(2, n+1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])


    return answer