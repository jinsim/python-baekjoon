# 메모이제이션 방식으로 풀었다. = 런타임에러
n = int(input())
dp = [0]*(n+1)
if n == 1:
    print(0)
elif n < 4:
    print(1)
else: 
    dp[1] = 0
    dp[2] = dp[3] = 1
    for i in range(4, n+1):
        if i % 3 == 0:
            if i % 2 == 0:
                dp[i] = min(dp[i//3], dp[i//2], dp[i-1])+1
            else:
                dp[i] = min(dp[i//3], dp[i-1])+1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1])+1
        else:
            dp[i] = dp[i-1] + 1
    print(dp[n])
        