import sys
input = sys.stdin.readline
T = int(input())

# 1로 DP 배열 초기화
dp = [1] * 10001

for j in range(2, 10001):  # 2이상부터 2 포함
    dp[j] += dp[j-2]

for j in range(3, 10001):  # 3이상부터 3 포함
    dp[j] += dp[j-3]

for i in range(T):
    n = int(input())
    print(dp[n])
