"""
집합 연산 구현
"""
import sys

S = set()

input = sys.stdin.readline

for _ in range(int(input())):
    exp = input().rstrip()
    if exp == "all":
        S = set([i for i in range(1, 21)])
        continue
    if exp == "empty":
        S = set()
        continue
    exp, num = exp.split()
    num = int(num)
    if exp == "add":
        S.add(num)
        continue
    if exp == "remove":
        if num in S:
            S.remove(num)
        continue
    if exp == "check":
        if num in S:
            print(1)
        else:
            print(0)
        continue
    if exp == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)
        continue