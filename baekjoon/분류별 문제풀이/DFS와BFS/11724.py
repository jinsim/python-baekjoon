# 연결 요소의 개수
# DFS로 연결 요소의 개수를 세면 된다. 중요한 것은 visited로 잘 끊어주는 것

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0] * (n+1)

def dfs(v):
    visited[v] = 1
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
    