"""
통상 길이가 N인 리스트에서 특정 원소의 유무 검사에는 O(N)이 걸린다. 그러나 Set을 활용할 경우 무조건 O(1), 즉 상수 시간으로 유무 검사를 해준다.
"""

# 리스트를 이용한 풀이. 3720ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [input() for _ in range(n)]
ret = 0

for _ in range(m):
    if input() in s:
        ret += 1

print(ret)

# set을 이용한 풀이. 152ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = {input() for _ in range(n)}
ret = 0 

for _ in range(m):
    if input() in s:
        ret += 1

print(ret)
