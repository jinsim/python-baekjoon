from collections import deque
N, K = map(int, input().split())
Q = deque()
Q.append(N)
V = [-1] * 100001
V[N] = N
while Q:
    v= Q.popleft()
    if v == K:
        break
    if not v == 0 and V[v-1] == -1:
        V[v-1] = v
        Q.append(v-1)
    if not v == 100000 and V[v+1] == -1:
        V[v+1] = v
        Q.append(v+1)
    if v <= 50000 and V[v*2] == -1:
        V[v*2] = v
        Q.append(v*2)
ret = [v]
while v != N:
    ret.append(V[v])
    v = V[v]
print(len(ret)-1)
ret.reverse()
print(*ret)