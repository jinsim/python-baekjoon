import sys
input = sys.stdin.readline
N, M = map(int, input().split())
memo = dict()
for _ in range(N):
    memo[input().rstrip()] = 1
ret = N
for _ in range(M):
    post = input().rstrip().split(sep=',')
    for p in post:
        if p in memo and memo[p]:
            memo[p] -= 1
            ret -=1
    print(ret)
