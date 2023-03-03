N = int(input())
O = list(map(int, input().split()))
V = list(map(int, input().split()))
ret = V[0]*O[0]
for i in range(1, N-1):
    V[i] = min(V[i], V[i-1])
    ret += O[i] * V[i]
print(ret)
