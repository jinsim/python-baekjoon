# DFS와 BFS
# DFS, BFS에 대한 이해를 볼 수 있는 문제

"""
graph를 defaultdict으로 구현했을 때 => graph를 이중 리스트로 구현했을 때 차이 없음.
visited로 결과 리스트를 만드는 것이 아닌, 방문햇을 때 바로 값을 출력했을 때 => 690ms에서 490ms로 단축
input을 변형했을 때 => 490ms에서 100ms으로 단축
"""

# 결과를 리스트로 반환
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = defaultdict(list)

def dfs(i):
    visited.append(i)
    for j in graph[i]:
        if j not in visited:
            dfs(j)
    return visited
    
def bfs(i):
    visited.append(i)
    queue = deque([i])
    while queue:
        for j in graph[queue.popleft()]:
            if j not in visited:
                visited.append(j)
                queue.append(j)
    return visited

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort()

visited = []
print(*dfs(v))
visited = []
print(*bfs(v))

# 바로 방문 노드 출력
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = defaultdict(list)

def dfs(i):
    print(i, end=' ')
    visited[i] = 1
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
    
def bfs(i):
    visited[i] = 1
    queue = deque([i])
    while queue:
        i = queue.popleft()
        print(i, end=' ')
        for j in graph[i]:
            if not visited[j]:
                visited[j] = 1
                queue.append(j)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort()

visited = [0] * (n+1)
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)
