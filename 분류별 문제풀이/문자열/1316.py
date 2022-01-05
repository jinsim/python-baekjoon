# 조건을 잘 파악하면 된다.
import sys
input = sys.stdin.readline
ret = int(input())
for _ in range(ret):
    l = []
    for i in input().strip():
        if i in l and l[-1] != i:
            ret -= 1
            break
        else:
            l.append(i)
print(ret)
