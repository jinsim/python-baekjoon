import bisect

N = int(input())
nums_N = list(map(int, input().split()))
M = int(input())
nums_M = map(int, input().split())
nums_N.sort()
for m in nums_M:
    i = bisect.bisect_left(nums_N, m)
    if i < N and nums_N[i] == m:
        print(1)
    else:
        print(0)