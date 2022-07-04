# 유기농 배추
# 인접한 노드 묶음의 개수를 구하면 된다. 쉽게 풀 수 있다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

for _ in range(int(input())):
    
    m, n, k = map(int, input().split())
    grid = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1
    
    def dfs(y, x):
        for dy, dx in move:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx]:
                grid[ny][nx] = 0
                dfs(ny, nx)
            
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                cnt += 1
                grid[i][j] = 0
                dfs(i, j)
    print(cnt)