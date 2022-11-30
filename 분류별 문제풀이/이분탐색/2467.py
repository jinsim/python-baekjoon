import sys

N = int(input())
liquid = list(map(int, input().split()))
min_val = sys.maxsize
va = ()
start = 0
end = N-1
while start < end:
    val = liquid[start] + liquid[end]
    if abs(min_val) > abs(val):
        min_val = val
        va = (start, end)
    if val > 0:
        end -= 1
    elif val < 0:
        start += 1
    else:
        break
print(liquid[va[0]], liquid[va[1]])

