# 섬의 개수
# 연결 요소의 개수를 세는 문제다. 이동할 수 있는 조건을 잘 파악해야한다. 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

move = []
for z in [-1,0,1]:
    for c in [-1,0,1]:
        move.append([z,c])
move.remove([0,0])

while True:
    w, h = map(int, input().split())
    if w == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(h)]

    def dfs(y, x):
        for dy, dx in move:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx]==1:
                grid[ny][nx] = 0
                dfs(ny, nx)
                
    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                grid[i][j] = 0
                dfs(i, j)
                cnt += 1

    print(cnt)