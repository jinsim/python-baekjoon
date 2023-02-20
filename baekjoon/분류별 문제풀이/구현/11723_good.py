"""
20까지의 숫자만 들어오므로, 집합에 해당 수가 있으면 1, 없으면 0으로 표시한다.
"""
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = [0 for _ in range(21)]

for _ in range(n):
    exp = input().rstrip()
    if exp == 'all':
        nums = [1 for _ in range(21)]
        continue
    elif exp == 'empty':
        nums = [0 for _ in range(21)]
        continue

    exp, num = exp.split()
    num = int(num)
    if exp == 'add':
        nums[num] = 1
        continue
    if exp == 'check':
        if nums[num]:
            print(str(1) + '\n')
        else:
            print(str(0) + '\n')
        continue
    if exp == 'remove':
        nums[num] = 0
        continue
    if exp == 'toggle':
        if nums[num]:
            nums[num] = 0
        else:
            nums[num] = 1
        continue