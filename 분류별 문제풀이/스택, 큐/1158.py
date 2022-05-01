# 덱의 문법에 대해 안다면 더욱 쉽게 풀 수 있다.
from collections import deque
n, k = map(int, input().split())
q = deque([i for i in range(1,n+1)])
ans = []
while q:
    q.rotate(-k+1)
    ans.append(q.popleft())
print('<'+str(ans)[1:-1]+'>')