import sys
from collections import deque
input = sys.stdin.readline

move = [[1,0],[-1,0],[0,1],[0,-1]]
R, C = map(int, input().split())
board = [input().strip('\n') for _ in range(R)]

visited=[["" for _ in range(C)] for _ in range(R)]

Q = deque()
Q.append((0,0,board[0][0]))
while Q:
    y, x, v = Q.popleft()
    ret = v
    for dy, dx in move:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in v:
            n = v+board[ny][nx]
            if visited[ny][nx] != n:
                visited[ny][nx] = n
                Q.append((ny, nx, n))
print(len(ret))