# DP로 풀이. SK 기준으로 이기는 경우를 True, 지는 경우를 False
# 1, 3 전일때 값 중 True가 있으면 False로 설정한다.
N = int((input()))
dp = [False]*(N+1)
dp[1] = True
if N > 2:
    dp[3] = True
    for i in range(4, N+1):
        dp[i] = not (dp[i-1] or dp[i-3])
print(dp)
print("SK" if dp[N] else "CY")



