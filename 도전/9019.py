from collections import deque

T = int(input())

def D(n):
    return 2*n % 10000

def S(n):
    n -= 1
    if not n:
        return 9999
    return n

def L(n):
    n *= 10
    n += n//10000
    n %= 10000
    return n

def R(n):
    n += (n%10)*10000
    n //= 10
    return n

def bfs(A, B):
    q = deque()
    q.append((A, ""))
    while q:
        word, cmd = q.popleft()
        if word == B:
            q.clear()
            break
        q.append((D(word), cmd+'D'))
        q.append((S(word), cmd+'S'))
        q.append((L(word), cmd+'L'))
        q.append((R(word), cmd+'R'))
    return cmd

for _ in range(T):
    A, B = map(int,input().split())
    print(bfs(A, B))

