# 단지번호붙이기
# 연결 요소 및 연결 요소내의 노드 개수 세기

"""
graph에서 dfs를 진행할 조건을 지정. dfs 내부에서 다음 재귀호출을 하는 조건 지정
각 dfs 별로 값을 낼 수 있게 하는 요소 설정
"""
n = int(input())
graph = [list(input()) for _ in range(n)]
move = [[0,1],[0,-1],[1,0],[-1,0]]
m = len(graph[0])

def dfs(y, x):
    global cnt
    cnt += 1
    for dy, dx in move:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == '1':
                graph[ny][nx] = '0'
                dfs(ny, nx)

cnt = 0
ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            graph[i][j] = '0'
            dfs(i,j)
            ans.append(cnt)
            cnt = 0

ans.sort()
print(len(ans), *ans, sep='\n')