import bisect
N, K = map(int, input().split())
moneys = []
for _ in range(N):
    moneys.append(int(input()))
cnt = 0
while True:
    idx = bisect.bisect_left(moneys, K)
    if idx != N:
        K - moneys[idx-1]
        cnt += 1
        continue
    val = moneys[idx]

    print(K, val)
    if K == val:
        break
    K -= moneys[bisect.bisect_left(moneys, K)-1]
    cnt += 1
print(cnt+1)

