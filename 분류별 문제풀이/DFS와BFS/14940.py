import sys
from collections import deque
# input = sys.stdin.readline
#표준입력을 파일로 설정
sys.stdin = open("../../input.txt","r")

move = [[1,0],[-1,0],[0,1],[0,-1]]
n, m = map(int, input().split())
ret=[[-1 for _ in range(m)] for _ in range(n)]

board = []
find = False
for i in range(n):
    lands = list(map(int,input().split()))
    for j in range(m):
        if not find and lands[j] == 2:
            s_y = i
            s_x = j
            find = True
        if not lands[j]:
            ret[i][j] = 0
    board.append(lands)

Q = deque()
Q.append((s_y, s_x))
ret[s_y][s_x] = 0
while Q:
    y, x = Q.popleft()
    for dy, dx in move:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx]:
            if ret[ny][nx] == -1 and not (ny == s_y and nx == s_x):
                ret[ny][nx] = ret[y][x]+1
                Q.append((ny, nx))

for i in range(n):
    print(*ret[i])