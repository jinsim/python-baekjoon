"""
DP 중 LIS(Longest Increasing Subsequence) 분류에 속하는 문제
주어진 배열에서 가장 길게 증가하는 부분 수열을 찾아내는 알고리즘이다.
하나씩 증가하며, 본인 이전의 수 중에서, 본인보다 작은 수들 중, 가장 긴 배열의 수에 1을 더한 값을 저장한다.
"""


N = int(input())
A = list(map(int, input().split()))
dp = [0]*N

for i in range(N):
    for j in range(0, i):
        if A[j] < A[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
