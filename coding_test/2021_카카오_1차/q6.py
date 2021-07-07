from itertools import permutations
from collections import deque

Board = [list() for i in range(4)]
card_pos = {}
d = [[0,1], [1,0], [0,-1], [-1,0]]
INF = 999999999
answer = INF
orders = []

def location(board):
    global Board, card_pos, orders
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card = board[i][j]
                if card not in card_pos.keys(): card_pos[card] = [[i,j]]
                else: card_pos[card].append([i,j])

            Board[i].append(board[i][j])
    

    orders = [key for key in card_pos.keys()]

    # 카드별 순열 경우의 수 찾기
    orders = list(permutations(orders))
          
def isin(y,x):
    if ((-1 < y < 4) & (-1 < x < 4)): return True
    return False

def move(y, x, mv):
    global Board
    ny, nx = y, x

    while True:
        _ny = ny + mv[0]
        _nx = nx + mv[1]
        if not isin(_ny, _nx): return ny, nx
        if Board[_ny][_nx] != 0: return _ny, _nx
            
        ny = _ny
        nx = _nx

def bfs(sy, sx, ey, ex):
    if [sy, sx] == [ey, ex]: return sy, sx, 1
    global Board
    q = []
    q = deque(q)
    table = [[0 for j in range(4)] for i in range(4)]
    visit = [[False for j in range(4)] for i in range(4)]
    q.append([sy, sx])
    visit[sy][sx] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if isin(ny, nx):
                if not visit[ny][nx]:
                    visit[ny][nx] = True
                    table[ny][nx] = table[y][x] + 1
                    if [ny,nx] == [ey,ex]:
                        return ny, nx, table[ny][nx] + 1

                    q.append([ny, nx])

            ny, nx = move(y, x, d[i])

            if not visit[ny][nx]:
                visit[ny][nx] = True      
                table[ny][nx] = table[y][x] + 1
                if [ny,nx] == [ey,ex]:
                    return ny, nx, table[ny][nx] + 1

                q.append([ny, nx])

    return sy, sx, INF
    
def backtrack(sy, sx, k, m, count):
    global orders, Board, answer, card_pos

    # 카드를 전부 찾았으면 리턴하기
    if k == len(card_pos.keys()):
        if answer > count: answer = count
        return

    # m번째 조합의 k번째 카드를 찾아보자
    card = orders[m][k]

    # 첫번째 카드 위치
    left_y, left_x = card_pos[card][0][0], card_pos[card][0][1]

    # 두번째 카드 위치
    right_y, right_x = card_pos[card][1][0], card_pos[card][1][1]


    # 카드 거리 찾기
    ry1, rx1, res1 = bfs(sy, sx, left_y, left_x)
    ry2, rx2, res2 = bfs(ry1, rx1, right_y, right_x)
    
    for y, x in card_pos[card]:
        Board[y][x] = 0
    backtrack(ry2, rx2, k+1, m, count + res1 + res2)
    for y, x in card_pos[card]: 
        Board[y][x] = card

    ry1, rx1, res1 = bfs(sy, sx, right_y, right_x)
    ry2, rx2, res2 = bfs(ry1, rx1, left_y, left_x)

    for y, x in card_pos[card]:
        Board[y][x] = 0
    backtrack(ry2, rx2, k+1, m, count + res1 + res2)
    for y, x in card_pos[card]:
        Board[y][x] = card

def solution(board, r, c):
    global answer
    location(board)

    for i in range(len(orders)):
        # i: 조합의 몇번째 순서를 시도하는건지
        # k: 해당 조합에서 몇번째 카드를 시도하는 건지
        backtrack(r, c, 0, i, 0)

    return answer