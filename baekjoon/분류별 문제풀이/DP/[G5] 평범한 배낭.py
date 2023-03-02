# [G5] 평범한 배낭
# 개수 N 무게 W 가치 V
# 배낭은 최대 K 개의 무게
"""
    0   1   2   3   4   5   6   7
0   0   0   0   0   0   0   0   0
1   0   0   0   0   0   0   13  13
2   0   0   0   0   8   8   13  13
3   0   0   0   6   8   8   13  14
4   0   0   0   6   8   12  13  14

"""
N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
li = []
for _ in range(N):
    li.append(list(map(int, input().split())))
for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= li[i-1][0]:
            dp[i][j] = max(li[i - 1][1]+dp[i-1][j-li[i - 1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
