import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    nums = list(map(int, input().rstrip().split()))
    nums.reverse()
    value = max = 0
    for num in nums:
        if(num > max):
            max = num
        else:
            value += max-num
    print(value)
