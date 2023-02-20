# 조건만 잘 파악하면 간단한 문제(가장 큰 값이 무조건 맨 뒤에 오지 않는다.)
while True:
    nums = sorted(map(int, input().split()))
    if nums[0] == 0:
        break
    if pow(nums[2], 2) == pow(nums[1], 2) + pow(nums[0], 2):
        print('right')
    else:
        print('wrong')
