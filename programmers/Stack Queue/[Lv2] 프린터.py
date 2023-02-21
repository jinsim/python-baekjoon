from collections import deque

def solution(priorities, location):
    Q = deque([(i, v) for i, v in enumerate(priorities)])
    cnt = 1
    max_val = max(priorities)
    while Q:
        i, v = Q.popleft()
        if v == max_val:
            if i == location:
                return cnt
            priorities.remove(v)
            max_val = max(priorities)
            cnt += 1
            continue
        Q.append((i, v))
    return cnt