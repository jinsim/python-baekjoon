# [S3] 계단 오르기
import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]
dp = [0] * (n)
if len(li)<=2:
    print(sum(li))
else:
    dp[0]=li[0]
    dp[1]=li[0]+li[1]
    for i in range(2,n):
        # i에 2가 들어가면 -1이 나오지만, 어차피 0으로 초기화되어 있어서 괜찮다.
        dp[i]=max(dp[i-3]+li[i-1]+li[i], dp[i-2]+li[i])
    print(dp[-1])