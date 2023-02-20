# 우선순위 큐로 풀이한 문제. 200ms
import heapq

N, M = map(int, input().split())
# 힙 생성(시간, 위치)
Q = [(0, N)]
# Q는 우선순위 최소 힙 큐이고, dist는 1씩 점점 늘어나므로 visited로 충분하다.
visited = [0] * 100001

while Q:
    dist, X = heapq.heappop(Q)
    visited[X] = 1
    if X == M:
        print(dist)
        break
    # 너무 많이 가지 않도록 조건을 설정해서 Heap에 삽입한다.
    if X*2 <= 2*M and X*2 <= 100000 and not visited[X*2]:
        heapq.heappush(Q, (dist, X*2))
    if X+1 <= 100000 and not visited[X+1]:
        heapq.heappush(Q, (dist+1, X+1))
    if 0 <= X-1 and not visited[X-1]:
        heapq.heappush(Q, (dist+1, X-1))