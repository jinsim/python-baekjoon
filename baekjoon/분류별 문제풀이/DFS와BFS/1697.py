# 숨바꼭질
# 최단 거리 찾기 문제. BFS

"""
핵심은 그래프에 cnt를 더해가며 저장하는 것이다. 
"""
from collections import deque
n, k = map(int, input().split())
graph = [0] * 100001
graph[n] = 1
Q = deque([n])

while Q:
    v = Q.popleft()
    if v == k:
        print(graph[v]-1)
        break
    for dv in [v-1, v+1, v*2]:
        if 0 <= dv < 100001 and graph[dv] == 0:
            graph[dv] = graph[v] + 1
            Q.append(dv)