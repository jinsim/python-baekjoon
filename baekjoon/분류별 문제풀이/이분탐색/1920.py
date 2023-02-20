N = int(input())
nums_N = list(map(int, input().split()))
M = int(input())
nums_M = map(int, input().split())
nums_N.sort()
for m in nums_M:
    left, right = 0, N - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums_N[mid] < m:
            left = mid+1
        elif nums_N[mid] > m:
            right = mid-1
        else:
            print(1)
            break
    else: print(0)