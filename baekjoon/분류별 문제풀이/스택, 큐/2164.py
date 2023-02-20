# deque를 사용해서 쉽게 풀 수 있다.
from collections import deque
n = int(input())
s = deque([i for i in range(1, n+1)])
for _ in range(n-1):
    s.popleft()
    s.append(s.popleft())
print(s[0])