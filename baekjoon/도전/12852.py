from collections import deque

N = int(input())

Q = deque((N, 0))
while Q:

if x % 3 == 0:
    x //= 3
if x % 2 == 0:
    x //= 2
x -= 1