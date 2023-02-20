# 스택에 대한 기본적인 이해만 있으면 풀 수 있는 문제.
import sys
input = sys.stdin.readline

s = []

for _ in range(int(input())):
    n = int(input())
    if n:
        s.append(n)
    else: 
        s.pop()
        
print(sum(s))