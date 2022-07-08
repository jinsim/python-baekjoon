# 미로 탐색 
# 미로 최단거리 찾기. BFS

"""
BFS는 최단 경로를 찾는 문제에서 주로 사용되며, 현재 경로와 가까운 경로부터 찾으므로 첫번째 나오는 답이 최단 거리가 된다.
DFS는 각 경로의 특징을 저장해야하는 제약 충족 문제에서 주로 사용되며, 완전 탐색 후 최단 거리를 구하므로 시간 초과가 쉽게 난다.
따라서 이 문제는 BFS로 푸는 것이 맞다.
"""

# DFS로 구현(시간초과)
from copy import deepcopy
n, m = map(int, input().split())
maze = [[] for _ in range(n)]
for i in range(n):
    maze[i] = list(input())
    
result = 999

def dfs(maze, cnt, y, x):
    if y >= n or x >= m or y < 0 or x < 0 or maze[y][x] == '0':
        return
    if y+1 == n and x+1 == m:
        global result
        result = min(result, cnt)
        return
    
    maze[y][x] = '0'
    cnt+=1
    dfs(deepcopy(maze), cnt, y+1, x)
    dfs(deepcopy(maze), cnt, y, x+1)
    dfs(deepcopy(maze), cnt, y-1, x)
    dfs(deepcopy(maze), cnt, y, x-1)
    
dfs([deepcopy(maze) for item in maze], 1, 0, 0)
print(result)

# BFS로 구현
from collections import deque
n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for i in range(n)]

move = [[0,1], [0,-1], [1,0], [-1,0]]

q = deque([[0,0]])

while q:
    y, x = q.popleft()
    if y+1 == n and x+1 == m:
        print(maze[y][x])
    for dy, dx in move:
        ny = dy+y
        nx = dx+x
        if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] ==1:
            maze[ny][nx] = maze[y][x] + 1
            q.append([ny, nx])


