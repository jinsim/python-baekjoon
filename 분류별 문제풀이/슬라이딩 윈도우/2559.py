N, K = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = K
s_sum = sum(A[:K])
ret = s_sum
while start < N-K:
    s_sum -= A[start]
    s_sum += A[start+K]
    start += 1
    ret = max(ret, s_sum)
print(ret)


