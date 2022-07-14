# 트리의 부모 찾기
# visited에 부모 노드를 채우며 BFS를 한다. 
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
Q = deque([1])
    
visited = [0]*(n+1)
visited[1] = 1
while Q:
    v = Q.popleft()
    
    for w in graph[v]:
        if not visited[w]:
            visited[w] = v
            Q.append(w)
    
print(*visited[2:], sep='\n')