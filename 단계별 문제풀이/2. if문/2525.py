h, m = map(int, input().split())
n = m + int(input())
while n >= 60:
    h += 1
    n -= 60
if h >= 24:
    h -= 24
print(h, n)