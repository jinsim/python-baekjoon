# set의 특징을 잘 알아야 풀 수 있다.
"""
그냥 풀면 시간초과나는 문제.
각각을 set으로 두고, 교집합을 구한 후, 정렬을 시킨다.
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(input().rstrip())
for _ in range(m):
    m_set.add(input().rstrip())
ret = sorted(n_set & m_set)
print(len(ret))
print("\n".join(ret))
