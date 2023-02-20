# N번째 큰 수
# 생각보다 쉽게 풀 수 있다.
"""
N번째 큰 수를 구하면 되므로, 숫자 N 개의 리스트를 내림차순으로 유지하면 된다.
그리고 제일 마지막 수를 출력하면 끝!
"""
import sys
input = sys.stdin.readline
num = int(input())
a = []
for _ in range(num):
    a.extend(list(map(int, input().split())))
    a.sort(reverse=True)
    a = a[:num]
print(a[-1])