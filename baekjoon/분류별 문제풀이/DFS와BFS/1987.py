import sys
input = sys.stdin.readline

move = [[1,0],[-1,0],[0,1],[0,-1]]
R, C = map(int, input().split())
board = [list(map(lambda x: ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(R)]
visited = [0] * 26
visited[board[0][0]] = 1
ret = 1

def dfs(y, x, cnt):
    global ret
    ret = max(ret, cnt)
    for dy, dx in move:
        ny = dy + y
        nx = dx + x
        if 0<=ny<R and 0<=nx<C and not visited[board[ny][nx]]:
            visited[board[ny][nx]] = 1
            dfs(ny, nx, cnt+1)
            visited[board[ny][nx]] = 0

dfs(0, 0, 1)
print(ret)