def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        if i == ')':
            if not stack or stack.pop() != '(':
                return False
    if stack:
        return False
    return True