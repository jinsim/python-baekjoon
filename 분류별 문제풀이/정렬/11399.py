# 쉬운 문제다. 정렬하고, 조건에 맞게 더해주면 된다.
num = int(input())
a = sorted(list(map(int, input().split())))
result = 0

for i, v in enumerate(a):
    result += (v*(num-i))

print(result)