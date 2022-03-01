# 파이썬 내부 sort()도 상당히 효율 좋은 로직이다.
import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    l.append(int(input().rstrip()))
l.sort()
print(*l, sep='\n')