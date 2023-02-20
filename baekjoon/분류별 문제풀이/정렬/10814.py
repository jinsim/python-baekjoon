# 람다를 이용한 리스트 정렬.

import sys
input = sys.stdin.readline
li = []
for _ in range(int(input())):
    li.append(input().rstrip())

li.sort(key=lambda x: int(x.split()[0]))
print(*li, sep='\n')