n = int(input())
S = list(map(int, input().split()))
ret = S[0]
tmp = 0
for i in range(n):
    tmp += S[i]
    ret = max(tmp, ret)
    if tmp < 0:
        tmp = 0
        continue
print(ret)
