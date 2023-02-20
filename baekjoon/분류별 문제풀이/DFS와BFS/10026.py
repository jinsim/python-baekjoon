# 적록색약

"""
두번의 반복문을 실행한다. 처음에는 R인 칸의 개수를 구하면서, G인 칸의 개수를 구하며 G를 R로 변경한다. 이 경우 나눠진 R과 G의 칸 수를 구할 수 있다.
그리고 visited를 초기화하고 R과 B의 칸 수를 센다.
"""
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
move = [[1,0],[-1,0],[0,1],[0,-1]]
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

def dfs(y, x):
    color = graph[y][x]
    if color == 'G':
        graph[y][x] = 'R'
        for dy, dx in move:
            ny = y + dy
            nx = x + dx
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and graph[ny][nx] == 'G':
                visited[ny][nx] = 1
                dfs(ny, nx)
    else:
        for dy, dx in move:
            ny = y + dy
            nx = x + dx
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and graph[ny][nx] == color:
                visited[ny][nx] = 1
                dfs(ny, nx)
    
cnt_G = cnt_GR = cnt_R = cnt_B = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' and not visited[i][j]:
            visited[i][j] = 1 
            dfs(i, j)
            cnt_GR += 1
        if graph[i][j] == 'G' and not visited[i][j]:
            visited[i][j] = 1 
            dfs(i, j)
            cnt_G += 1
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' and not visited[i][j]:
            visited[i][j] = 1 
            dfs(i, j)
            cnt_R += 1
        if graph[i][j] == 'B' and not visited[i][j]:
            visited[i][j] = 1 
            dfs(i, j)
            cnt_B += 1
print(cnt_GR+cnt_G+cnt_B, cnt_R+cnt_B)