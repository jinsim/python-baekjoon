import sys
input = sys.stdin.readline
total = int(input())
num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    total -= a*b

print("No" if total else "Yes")