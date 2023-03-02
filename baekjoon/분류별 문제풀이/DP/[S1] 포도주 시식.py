# [S1] 포도주 시식
import sys
input = sys.stdin.readline
n = int(input())
podo = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(podo))
else:
    dp = [0] * (n)
    dp[0] = podo[0]
    dp[1] = podo[0] + podo[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3] + podo[i-1] + podo[i], dp[i-2] + podo[i], dp[i-1])
    print(max(dp))