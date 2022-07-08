# 바이러스
# 연결 요소에 포함된 노드 개수 구하기

"""
숫자형태로 변형해서 그래프를 생성하고, 방문한 요소는 True로 두어 연결된 노드 중 방문하지 않은 노드에 대해서만 dfs를 재귀 호출한다. 호출한 수가 연결된 노드의 수이다.
"""
from collections import defaultdict
maze = defaultdict(list)
n = int(input())
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    maze[a].append(b)
    maze[b].append(a)

visited = [False]*(n+1)
cnt = 0

def dfs(i):
    global cnt
    visited[i] = True
    for j in maze[i]:
        if not visited[j]:
            dfs(j)
            cnt += 1
        
dfs(1)
print(cnt)