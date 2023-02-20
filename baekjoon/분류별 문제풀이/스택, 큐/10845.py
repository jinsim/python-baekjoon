# 큐에 대한 기본적인 이해만 있으면 풀 수 있는 문제
# 스택과 마찬가지로, 파이썬의 리스트로 모든 연산을 사용 가능 하지만, 
# 리스트는 동적 배열이므로 큐의 연산을 수행하기 효율적이지 않다. 덱을 사용하자.
from collections import deque
import sys
input = sys.stdin.readline
stack = deque()
for _ in range(int(input())):
    cmd_full = input()
    cmd = cmd_full.split()[0]
    if cmd == 'push':
        stack.append(cmd_full.split()[1])
    elif cmd == 'pop':
        print(stack.popleft() if len(stack) else -1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(0 if len(stack) else 1)
    elif cmd == 'front':
        print(stack[0] if len(stack) else -1)
    elif cmd == 'back':
        print(stack[-1] if len(stack) else -1)