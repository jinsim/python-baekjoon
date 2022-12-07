"""
DP 중 LIS 문제를 활용했다. 11053 문제를 참고하면 좋다.
"""
import sys
input = sys.stdin.readline

N = int(input())
A = []
dp = [0]*N

for _ in range(N):
    A.append(int(input()))

for i in range(N):
    for j in range(0, i):
        if A[j] < A[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(N-max(dp))