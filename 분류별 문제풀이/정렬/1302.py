# 람다를 사용하면 쉽게 풀 수 있다.
import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())
d = defaultdict(int)
for _ in range(n):
    d[input()] += 1
print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])