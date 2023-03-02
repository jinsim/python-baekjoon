# [S1] 쉬운 계단 수
"""
자리, 끝나는 수
    0 1 2 3 4 5 6 7 8 9
0   0 0 0 0 0 0 0 0 0 0
1   0 1 1 1 1 1 1 1 1 1
2   1 1 2 2 2 2 2 2 2 1
3   1 3 3 4 4 4 4 4 3 2
"""
n = int(input())
dp = [[0]*10 for _ in range(n)]
dp[0] = [0] + [1] * 9
for i in range(1, n):
    for j in range(10):
        if not j == 0:
            dp[i][j] += dp[i-1][j-1]
        if not j == 9:
            dp[i][j] += dp[i-1][j+1]
print(sum(dp[-1])%1000000000)