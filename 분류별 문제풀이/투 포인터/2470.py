import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
left = 0
right = N-1
ret = sys.maxsize
ret_l = A[0]
ret_r = A[N-1]
while left < right:
    ssum = A[left] + A[right]
    if abs(ssum) < ret:
        ret = abs(ssum)
        ret_l = A[left]
        ret_r = A[right]
    if ssum > 0:
        right -= 1
    else:
        left += 1
print(ret_l, ret_r)