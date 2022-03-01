# 입력가능한 N은 10000이하, 입력 횟수는 무려 10,000,000이다. cnt를 세자!
import sys
input = sys.stdin.readline

l = [0]*10001
for _ in range(int(input())):
    l[int(input().rstrip())] += 1

for i in range(10001):
    for _ in range(l[i]):
        print(i)