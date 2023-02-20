N, M = map(int, input().split())
A = list(map(int, input().split())) + [0]

left, right, ret = 0, 0, A[0]
cnt = 0
while right < N:
    if ret == M:
        right += 1
        ret += A[right]
        ret -= A[left]
        left += 1
        cnt += 1
        continue
    if ret < M:
        right += 1
        ret += A[right]
        continue
    if ret > M:
        ret -= A[left]
        left += 1
        continue
print(cnt)