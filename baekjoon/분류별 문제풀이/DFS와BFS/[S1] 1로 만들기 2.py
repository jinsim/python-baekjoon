# [S1] 1로 만들기 2
import sys
from collections import deque
N = int(input())
dp = [[] for _ in range(N+1)]
INF = sys.maxsize
Q = deque()
Q.append(N)
while Q:
    v = Q.popleft()
    if v == 1:
        break
    if v % 3 == 0 and not dp[v // 3]:
        # 이전까지 방문한 노드
        dp[v // 3] = dp[v] + [v]
        # 다음 요소
        Q.append(v//3)
    if v % 2 == 0 and not dp[v // 2]:
        dp[v // 2] = dp[v] + [v]
        Q.append(v//2)
    if v > 1 and not dp[v-1]:
        dp[v - 1] = dp[v] + [v]
        Q.append(v-1)
print(len(dp[1]))
print(*dp[1],1)
