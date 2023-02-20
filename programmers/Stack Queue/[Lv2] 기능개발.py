import math

def solution(progresses, speeds):
    n = len(progresses)
    end = []  # [7, 3, 9]
    ret = []
    for i in range(n):
        end.append(math.ceil(((100 - progresses[i]) / speeds[i])))

    left = right = 0
    while left < n:
        while right < n:
            if end[left] >= end[right]:
                right += 1
                continue
            break
        ret.append(right - left)
        left = right
    return ret