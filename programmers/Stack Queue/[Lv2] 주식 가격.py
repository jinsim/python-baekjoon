def solution(prices):
    n = len(prices)
    stack = []
    ret = [0] * n

    for i, v in enumerate(prices):
        while stack and stack[-1][1] > v:
            ret[stack.pop()[0]] = i - stack[-1][0]
        stack.append((i, v))

    for i in stack:
        ret[i[0]] = n-1-i[0]
    return ret