import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
times = [INF for _ in range(N + 1)]
times[1] = 0

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((i, b))
    graph[b].append((i, a))

Q = [(0, 1)]

while Q:
    t, n = heapq.heappop(Q)
    if n == N:
        print(t)
        break
    for dest_t, dest_n in graph[n]:
        total_t = (dest_t - t) % M + t + 1
        if total_t < times[dest_n]:
            times[dest_n] = total_t
            heapq.heappush(Q, (total_t, dest_n))