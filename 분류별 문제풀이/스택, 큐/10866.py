# deque에 대한 문법만 알면 쉽게 풀 수 있다.
from collections import deque
import sys
input = sys.stdin.readline

deq = deque()
for _ in range(int(input())):
    inp = input()
    cmd = inp.split()[0]
    if cmd == "pop_front":
        print(deq.popleft() if deq else -1)
    elif cmd == "pop_back":
        print(deq.pop() if deq else -1)
    elif cmd == "size":
        print(len(deq))
    elif cmd == "empty":
        print(0 if deq else 1)
    elif cmd == "front":
        print(deq[0] if deq else -1)
    elif cmd == "back":
        print(deq[-1] if deq else -1)
    elif cmd == "push_front":
        deq.appendleft(inp.split()[1])
    else: deq.append(inp.split()[1])