# 나이트의 이동
# BFS로 최단 거리를 측정하면 된다. 나이트의 이동 경우를 리스트로 만들어둔다.
from collections import deque
import sys
input = sys.stdin.readline

move = [[1,2],[2,1],[-1,2],[-2,1],[-1,-2],[-2,-1],[1,-2],[2,-1]]
for _ in range(int(input())):
    n = int(input())
    x, y = map(int,input().split())
    end_x, end_y = map(int,input().split())
    graph = [[0]*n for _ in range(n)]
    Q = deque([[y, x]])
    
    while Q:
        y, x = Q.popleft()
        if y == end_y and x == end_x:
            print(graph[y][x])
            break
        for dy, dx in move:
            ny = y + dy
            nx = x + dx
            if 0<=ny<n and 0<=nx<n and not graph[ny][nx]:
                graph[ny][nx] = graph[y][x] + 1
                Q.append([ny, nx])
