import sys

N, S = map(int, input().split())
A = list(map(int, input().split())) + [0]
left = right = 0
ssum = A[0]
ret = sys.maxsize

while right < N:
    if ssum < S:
        right += 1
        ssum += A[right]
    else:
        ret = min(ret, right - left + 1)
        ssum -= A[left]
        left += 1
print(0 if ret > N else ret)
