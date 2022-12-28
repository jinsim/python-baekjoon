import sys
import heapq
input = sys.stdin.readline

move = [[1,0],[-1,0],[0,1],[0,-1]]
R, C = map(int, input().split())
board = [input().strip('\n') for _ in range(R)]

visited=[["" for _ in range(C)] for _ in range(R)]

Q = [(1, 0, 0, board[0][0])]
while Q:
    l, y, x, v = heapq.heappop(Q)
    ret = l
    for dy, dx in move:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in v:
            n = v+board[ny][nx]
            if visited[ny][nx] != n:
                visited[ny][nx] = n
                Q.append((l+1, ny, nx, v+board[ny][nx]))
print(ret)