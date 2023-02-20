# 안전 영역
# 범위를 정하고, 연결요소의 개수를 구하는 로직을 짜면 된다. 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

move = [[1,0],[-1,0],[0,1],[0,-1]]
n = int(input())
graph = []
max_height = 0
min_height = 101
for _ in range(n):
    li = list(map(int, input().split()))
    graph.append(li)
    max_height = max(max_height, max(li))
    min_height = min(min_height, min(li))

def dfs(y, x, max_height):
    for dy, dx in move:
        ny = dy + y
        nx = dx + x
        if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and graph[ny][nx]>max_height:
            visited[ny][nx] = 1
            dfs(ny, nx, max_height)

max_cnt = 0
while min_height <= max_height:
    cnt = 0
    max_height -= 1
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j]>max_height:
                visited[i][j] = 1
                dfs(i, j, max_height)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)