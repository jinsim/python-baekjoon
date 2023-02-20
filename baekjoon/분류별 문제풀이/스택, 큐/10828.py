# 스택에 대한 기본적인 이해만 있으면 풀 수 있는 문제
import sys
input = sys.stdin.readline
stack = []
for _ in range(int(input())):
    cmd_full = input()
    cmd = cmd_full.split()[0]
    if cmd == 'push':
        stack.append(cmd_full.split()[1])
    elif cmd == 'pop':
        print(stack.pop() if len(stack) else -1)
    elif cmd == 'top':
        print(stack[-1] if len(stack) else -1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(0 if len(stack) else 1)