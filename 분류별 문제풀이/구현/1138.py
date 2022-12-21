"""
1부터 왼쪽부터 0의 개수를 센 후, 그 다음에 나오는 0에 해당 숫자를 넣으면 된다.
"""
N = int(input())
li = [0]*N
inp = map(int, input().split())
for idx, val in enumerate(inp):
    cnt = 0
    tmp = 0
    for i in li:
        if cnt == val:
            break
        if not i:
            cnt+=1
        tmp+=1
    for i in range(tmp, N):
        if not li[i]:
            li[i] = idx + 1
            break
print(*li)
