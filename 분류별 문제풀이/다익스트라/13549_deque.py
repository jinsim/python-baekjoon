# 덱으로 풀이한 문제. 156ms. 더 빠르다.
# dist로 우선순위를 잴 필요 없이, 순간이동일 때는 무조건 우선순위를 높게 주면 되므로 덱으로 충분하다.
from collections import deque

N, M = map(int, input().split())
# 덱 생성(시간, 위치)
Q = deque()
Q.append((0, N))
visited = [0] * 100001

while Q:
    dist, X = Q.popleft()
    visited[X] = 1
    if X == M:
        print(dist)
        break
    # 순간이동일 경우에는 시간이 늘지 않아 우선순위가 가장 높으므로 left에 넣는다.
    if X*2 <= 2*M and X*2 <= 100000 and not visited[X*2]:
        Q.appendleft((dist, X*2))
    if X+1 <= 100000 and not visited[X+1]:
        Q.append((dist+1, X+1))
    if 0 <= X-1 and not visited[X-1]:
        Q.append((dist+1, X-1))