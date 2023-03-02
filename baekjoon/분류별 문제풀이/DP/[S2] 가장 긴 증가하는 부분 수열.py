# [S2] 가장 긴 증가하는 부분 수열
n = int(input())
A = list(map(int, input().split()))
dp = [1] * (n+1)
for i in range(1, n):
    for j in range(i):
        if A[i] > A[j] and dp[j] >= dp[i]:
            dp[i] = dp[j]+1
print(max(dp))