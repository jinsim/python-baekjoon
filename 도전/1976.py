import sys
from collections import defaultdict

#표준입력을 파일로 설정
sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = defaultdict(list)
for i in range(1, N+1):
    link = list(map(int, input().split()))
    for j in range(1, N+1):
        if link[j-1]:
            graph[i].append(j)
order = list(map(int, input().split()))

visited = []
visited.append(order[0])
ret = 1
def dfs(v):
    global visited
    global ret
    if ret >= M:
        return True
    if v == order[ret]:
        if ret == M:
            return True
        else:
            ret += 1
            visited = []
    for i in graph[v]:
        if i not in visited:
            visited.append(i)
            dfs(i)
    return False
dfs(order[0])
print("YES" if ret>=M else "NO")
